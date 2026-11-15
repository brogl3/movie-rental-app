# Movie rental app - OOP refactor

The console interface retains the original semicolon syntax, for example:

    add movie; Shrek; Animation; An ogre's adventure; 12
    add client; John; 5010101123456
    add rental; 1; 1; 01/11/2026; 10/11/2026
    show movies
    undoM
    exit

Run `python main.py` to start with demonstration data, or `python tests.py` to run tests.

## Structure

- `domain_movies.py`, `domain_clients.py`, `domain_rentals.py`: domain classes.
- `repository_movies.py`, `repository_clients.py`, `repository_rentals.py`: independent repositories and undo histories.
- `repository.py`: `RepositoryManager` for dependency wiring and sample data.
- `validation.py`: `Validator` for state-aware checks.
- `readers.py`: `InputReader` for conversion and normalization.
- `commands.py`: `CommandHandler` with command metadata and dispatch.
- `command_process.py`: `CommandProcessor` for argument-code parsing.
- `ui.py`: `ConsoleUI` for parsing and the interactive loop.
- `helpers.py`: stateless pure helper functions (left as functions intentionally).
- `main.py`: application composition root.

## Notes

IDs belong to each repository, not a module-level/class-level global, allowing multiple independent application instances. Movies and clients with active rentals (today is between rental start and due dates, inclusive) cannot be deleted. Deleting an entity with only past or future rentals still follows the existing cascading behavior. Cascading deletions save the deleted rentals with the corresponding movie/client history entry; `undoM` or `undoC` restores that related deletion. `undoR` remains independent for explicit rental operations. The program is in-memory only, as in the original version. For production use, rental-related invariants and edit/delete behavior would need further decisions.
