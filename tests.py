"""Run with python tests.py (stdlib assertions, no external dependencies)."""
from main import createApplication
from datetime import date, timedelta
from helpers import isDate, isLeap, dateToDays, isDatePair


def assertRaisesValueError(fn):
    try:
        fn()
    except ValueError:
        return
    assert False, 'Expected ValueError'


def testHelpers():
    assert isLeap('01/01/2024')
    assert not isLeap('01/01/1900')
    assert isLeap('01/01/2000')
    assert isDate('29/02/2024')
    assert not isDate('29/02/2026')
    assert not isDate('31/04/2026')
    assert dateToDays('01/03/2024') - dateToDays('28/02/2024') == 2
    assert not isDatePair(('11/11/2026', '10/11/2026'))


def testCommands():
    ui, r = createApplication(with_sample_data=False)
    assert ui.parse('add movie; Shrek; Comedy; ogre; 3') == ('add movie', ['Shrek', 'Comedy', 'ogre', '3'])
    ui.executeInput('add movie; Shrek; Comedy; ogre; 3')
    assert r.movies.getMovieById(1).getTitle() == 'Shrek'
    ui.executeInput('edit movie; 1; Shrek 2; Comedy; sequel; 5')
    assert r.movies.getMovieById(1).getCopies() == 5
    ui.executeInput('undoM')
    assert r.movies.getMovieById(1).getTitle() == 'Shrek'
    ui.executeInput('add client; John; 1234567890123')
    ui.executeInput('add rental; 1; 1; 01/11/2026; 10/11/2026')
    assert r.rentals.getRentalById(1).getcId() == 1
    assertRaisesValueError(lambda: ui.executeInput('add rental; 1; 1; 20/11/2026; 10/11/2026'))
    assertRaisesValueError(lambda: ui.executeInput('add movie; missing fields'))
    assertRaisesValueError(lambda: ui.executeInput('unknown command'))


def testCascadeAndUndo():
    ui, r = createApplication(with_sample_data=False)
    ui.executeInput('add movie; Shrek; Animation; ogre; 3')
    ui.executeInput('add client; John; 1234567890123')
    ui.executeInput('add rental; 1; 1; 01/11/2026; 10/11/2026')
    ui.executeInput('delete movie; 1')
    assert not r.movies.movieExists(1)
    assert not r.rentals.rentalExists(1)
    ui.executeInput('undoM')
    assert r.movies.movieExists(1)
    assert r.rentals.rentalExists(1)
    ui.executeInput('delete client; 1')
    assert not r.clients.clientExists(1)
    assert not r.rentals.rentalExists(1)
    ui.executeInput('undoC')
    assert r.clients.clientExists(1)
    assert r.rentals.rentalExists(1)




def testActiveRentalDeletionProtection():
    ui, r = createApplication(with_sample_data=False)
    ui.executeInput('add movie; Shrek; Animation; ogre; 3')
    ui.executeInput('add client; John; 1234567890123')

    today = date.today()
    start = (today - timedelta(days=1)).strftime('%d/%m/%Y')
    due = (today + timedelta(days=1)).strftime('%d/%m/%Y')

    ui.executeInput(f'add rental; 1; 1; {start}; {due}')
    assertRaisesValueError(lambda: ui.executeInput('delete movie; 1'))
    assertRaisesValueError(lambda: ui.executeInput('delete client; 1'))

    assert r.movies.movieExists(1)
    assert r.clients.clientExists(1)
    assert r.rentals.rentalExists(1)

    # Rejected deletions must not create undo history entries.
    # Each repository has one history entry from the initial add.
    assert len(r.movies._history) == 1
    assert len(r.clients._history) == 1
    assert r.rentals.rentalExists(1)

    # A second application proves that future rentals do not count as current.
    ui2, r2 = createApplication(with_sample_data=False)
    ui2.executeInput('add movie; Future Movie; Sci-Fi; Space; 2')
    ui2.executeInput('add client; Jane; 2345678901234')
    future_start = (today + timedelta(days=2)).strftime('%d/%m/%Y')
    future_due = (today + timedelta(days=5)).strftime('%d/%m/%Y')
    ui2.executeInput(f'add rental; 1; 1; {future_start}; {future_due}')
    ui2.executeInput('delete movie; 1')
    assert not r2.movies.movieExists(1)
    assert not r2.rentals.rentalExists(1)

    # Expired rentals also do not prevent deletion.
    ui3, r3 = createApplication(with_sample_data=False)
    ui3.executeInput('add movie; Old Movie; Drama; Story; 2')
    ui3.executeInput('add client; Bob; 3456789012345')
    past_start = (today - timedelta(days=5)).strftime('%d/%m/%Y')
    past_due = (today - timedelta(days=2)).strftime('%d/%m/%Y')
    ui3.executeInput(f'add rental; 1; 1; {past_start}; {past_due}')
    ui3.executeInput('delete client; 1')
    assert not r3.clients.clientExists(1)
    assert not r3.rentals.rentalExists(1)


def testIndependentInstances():
    _, first = createApplication(False)
    _, second = createApplication(False)
    first.movies.addMovie('Shrek', 'Animation', 'Ogre', 10)
    assert first.movies.movieExists(1)
    assert not second.movies.movieExists(1)
    assertRaisesValueError(second.movies.undoM)


def testSampleData():
    _, repos = createApplication(True)
    assert len(repos.movies.getAllMovies()) == 10
    assert len(repos.clients.getAllClients()) == 6
    assert len(repos.rentals.getAllRentals()) == 6
    assertRaisesValueError(repos.movies.undoM)


def runAllTests():
    for test in [testHelpers, testCommands, testCascadeAndUndo, testActiveRentalDeletionProtection, testIndependentInstances, testSampleData]:
        test()
        print('[PASS]', test.__name__)
    print('All tests passed!')


if __name__ == '__main__':
    runAllTests()
