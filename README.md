# Student Task Manager

[![Tests](https://github.com/Moeez-rashid/student-task-manager/actions/workflows/tests.yml/badge.svg)](https://github.com/Moeez-rashid/student-task-manager/actions/workflows/tests.yml)

A small Python console application for keeping track of student tasks — assignments, quizzes, readings — built for the **CSC418 DevOps for Cloud Computing** lab (Assignment 4) to practise a complete Git and GitHub workflow.

Project status: v1.0.0 released — core features complete and covered by automated tests

## Features

- **Add tasks** — titles are trimmed; empty, whitespace-only and over-100-character titles are rejected.
- **Display tasks** — each task shows `[ ]` (pending) or `[x]` (completed) with its id.
- **Complete tasks** — mark one task or several selected tasks at once (e.g. `1,3`); already-completed and unknown ids are reported.
- **Delete tasks** — only a valid, existing task id is accepted, with a `y/n` confirmation.
- **Saved between runs** — tasks are stored in `tasks.json` next to the program.

## Setup

Requirements: **Python 3.8+** (no third-party packages).

```bash
git clone https://github.com/Moeez-rashid/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python main.py
```

```
===== Student Task Manager =====
1. Add task
2. Display tasks
3. Mark task as completed
4. Delete task
0. Exit
```

Choose a number and follow the prompts. See the [user guide](docs/user-guide.md) for a full walkthrough.

## Running the tests

```bash
python -m unittest discover -s tests -v
```

The same command runs automatically in GitHub Actions ([`.github/workflows/tests.yml`](.github/workflows/tests.yml)) on every push to `main` and every pull request to `main`.

## Project structure

```
student-task-manager/
├── main.py                  # console menu (input/output only)
├── task_manager.py          # Task model, TaskManager logic, JSON persistence
├── tests/
│   └── test_task_manager.py # unittest suite
├── docs/
│   └── user-guide.md        # how to use the app
├── .github/workflows/
│   └── tests.yml            # CI workflow
├── LAB-REPORT.md            # assignment report (Part G)
└── lab-evidence/            # screenshots of key steps
```

## License

[MIT](LICENSE)
