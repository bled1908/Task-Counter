# Cute Task Counter


An uncomplicated desktop application implemented in Python using the Tkinter graphical toolkit. The application provides a minimal workflow to set and decrement a task counter, displays contextual motivational messages, and presents a visual progress indicator.

<p align="center"><img src="public/Initial%20Pic.png" alt="Initial screen" /></p>

## Overview

The primary goal of this project is to offer a lightweight, distraction-minimizing utility to track outstanding tasks. It is suitable for personal use and for packaging as a standalone executable for distribution on Windows.

## Features

- Lightweight GUI built with the Python standard library (`tkinter`).
- Persistent local state saved to `counter_state.txt` (excluded from version control).
- Visual progress indicator (flower stages) and randomized motivational messages.
- Completion notification via a short chime using the Windows `winsound` API.
- Packaging support via PyInstaller (`task_counter.spec` included).

## Screenshots


Set starting count

<p align="center"><img src="public/task%20set%20pic.png" alt="Set starting count" /></p>


All tasks completed

<p align="center"><img src="public/task%20completed.png" alt="Tasks completed" /></p>

## Requirements

- Python 3.8 or later on Windows for full feature parity. The application uses only standard library modules: `tkinter`, `winsound`, `os`, and `random`.

## Installation and Execution

1. Open PowerShell and change to the project directory:

```powershell
cd 'C:\Projects\Task Counter'
```

2. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

3. Execute the application:

```powershell
python task_counter.py
```

Follow on-screen prompts: enter a starting count using the input field and press "Set Starting Count". Use "I finished one!" to decrement the counter.

## Packaging (Optional)

To create a single-file Windows executable, use PyInstaller with the included spec file:

```powershell
pyinstaller --onefile task_counter.spec
```

The produced artifact will appear in the `dist/` directory.

## Repository Contents

- `task_counter.py` — Application source code.
- `task_counter.spec` — PyInstaller specification for building an executable.
- `public/` — Images used in this README.
- `LICENSE` — Project license (MIT).
- `.gitignore` — Files and directories excluded from version control.

## License

This project is licensed under the MIT License. See the `LICENSE` file for the full text and attribution requirements.

## Contributing

Contributions are welcome. Please follow these guidelines when proposing changes:

1. Open an issue to discuss substantial changes before submitting a pull request.
2. Fork the repository and create a branch for your change: `git checkout -b feature/your-feature`.
3. Keep changes focused and implement tests or verification steps where appropriate.
4. Follow the existing code style and prefer simple, well-documented changes.

To submit a change, create a pull request from your branch to `main`. For questions or to discuss contributions directly, contact the project maintainer at: `bled19082005@gmail.com`.

## Contact

For support or inquiries, email: `bled19082005@gmail.com`.

