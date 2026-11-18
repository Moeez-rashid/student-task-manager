# Student Task Manager — User Guide

## Starting the program

Open a terminal in the project folder and run:

```bash
python main.py
```

The main menu appears. Type the number of an option and press **Enter**.

| Option | What it does |
|---|---|
| `1` | Add a task |
| `2` | Display all tasks |
| `3` | Mark one or more tasks as completed |
| `4` | Delete a task |
| `0` | Exit |

Your tasks are saved automatically to `tasks.json` after every action, so they are still there the next time you start the program.

## Adding a task

Choose `1` and type a title, for example `Submit DevOps lab`.

- Extra spaces at the start or end are removed.
- An empty title is refused: `Error: Task title cannot be empty.`
- Titles can be up to 100 characters.

## Displaying tasks

Choose `2`:

```
[ ] 1. Submit DevOps lab
[x] 2. Revise for quiz
```

`[x]` means completed, `[ ]` means still pending. The number is the task **id** used by the other options.

## Completing tasks

Choose `3`, then enter one id (`2`) or several ids separated by commas (`1,3`).

```
Task 1 marked as completed.
Task 3 was already completed.
Task 9 not found.
```

## Deleting a task

Choose `4`, enter the task id, then confirm with `y` (anything else cancels).

- Letters or symbols are refused: `Error: the task id must be a positive whole number.`
- An id that does not exist is refused: `Error: No task with id 7.`

## Starting fresh

Delete the `tasks.json` file while the program is closed to remove all saved tasks.
