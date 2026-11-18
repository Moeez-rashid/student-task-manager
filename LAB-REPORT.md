# Lab Report — Assignment 4: Student Task Manager with Git and GitHub

| | |
|---|---|
| **Name** | Moeez Rashid |
| **Roll No.** | FA23-BSE-083 |
| **Course** | CSC418 — DevOps for Cloud Computing |
| **Instructor** | Dr. M. Hasanain Ch |
| **Repository** | https://github.com/Moeez-rashid/student-task-manager |
| **Release** | https://github.com/Moeez-rashid/student-task-manager/releases/tag/v1.0.0 |

## 1. Git vs GitHub; `add`, `commit` and `push`

**Git** is the version-control tool that runs on my own computer. It records snapshots of the project, keeps the full history and lets me create branches, all without needing the internet. **GitHub** is a website that hosts Git repositories online. It adds things Git does not have on its own: a shared remote copy, Issues, Pull Requests with code review, Actions for CI, and Releases.

- `git add` moves changes into the **staging area** — I choose exactly which changes go into the next commit.
- `git commit` saves the staged changes as a permanent snapshot in my **local** history, with a message explaining why.
- `git push` uploads my local commits to the **remote** (GitHub) so others, and CI, can see them.

## 2. Why branches and Pull Requests; what causes merge conflicts

A **branch** is an independent line of work. I built each feature (`feature/add-task`, `feature/complete-task`, `feature/delete-task`) on its own branch so unfinished code never broke `main`, the features could be developed and reviewed separately, and the commit graph shows clearly where each feature came from.

A **Pull Request** asks to merge a branch into `main`. It shows the changed files, lets a reviewer comment on specific lines, runs the CI tests automatically, and links to the Issue it closes (`Closes #1`), so the history explains *why* each change was made.

A **merge conflict** happens when two branches change the **same lines** of the same file in different ways since their common ancestor. Git cannot know which version is correct, so it stops and marks the file with `<<<<<<<`, `=======` and `>>>>>>>`. In Part D both `status/in-progress` and `status/testing` rewrote the `Project status: Planning` line in `README.md`. The first merge succeeded; the second one conflicted. I kept one combined line that includes both updates, removed the markers, then ran `git add` and `git commit` to finish the merge.

## 3. `fetch` vs `pull`; `merge` vs `rebase`

- `git fetch` downloads new commits from the remote and updates `origin/main`, but **does not change my working files or my branch**. I can inspect the changes first.
- `git pull` is `fetch` **plus** an integration step (a merge by default) into my current branch — it updates my files immediately. In Part A I edited the README on GitHub and used `git pull` to bring it into my local copy.

- `git merge` joins two branches by creating a **merge commit** with two parents. History is kept exactly as it happened (the graph shows the branch and the join).
- `git rebase` **re-applies** my commits on top of another branch, creating new commits. The history becomes a straight line and is cleaner to read, but because commits are rewritten it should not be used on branches other people already use.

## 4. How Issues and Actions help a team

**GitHub Issues** are a shared to-do list. Each piece of work (feature, validation, tests, docs) gets an Issue with a description and a label, so the team knows what is planned, who is working on it and what is finished. Linking a PR with `Closes #n` closes the Issue automatically when the work is merged.

**GitHub Actions** runs automation on GitHub's servers. My workflow runs the unit tests on every push to `main` and every PR to `main`. Problems are caught before merging: the first run of PR #9 **failed** because of a wrong assertion, and only after the fix did the check turn green and the PR get merged. Nobody has to remember to run the tests by hand.

## 5. One difficulty and how I solved it

While collecting evidence for the branch comparison I ran a loop like `git show $b:task_manager.py` in my terminal (zsh) and got `fatal: ambiguous argument 'add-taskask_manager.py'`. The `t` had disappeared from the file name. The cause was that zsh treats `:t` after a variable as a *modifier* (it means "tail of the path"), so `$b:t…` was rewritten before Git ever saw it. I fixed it by putting braces and quotes around the variable — `git show "${b}:task_manager.py"` — and the command worked.

A second, smaller problem was planning the three feature branches: all of them edit `task_manager.py` and `main.py`. I kept each feature's changes inside its own function so Git could merge all three PRs automatically, and checked this with a trial merge on a temporary branch before opening the PRs.

## Evidence summary (Part H)

| Requirement | Achieved | Where |
|---|---|---|
| ≥ 12 meaningful commits | ✅ | `git log` / [commits](https://github.com/Moeez-rashid/student-task-manager/commits/main) |
| 3 feature branches | ✅ | `feature/add-task`, `feature/complete-task`, `feature/delete-task` (+ `feature/tests-ci`, `docs/readme-user-guide`) |
| 4 Issues with labels | ✅ 5 | [Issues #1–#5](https://github.com/Moeez-rashid/student-task-manager/issues?q=is%3Aissue) |
| 5 merged Pull Requests | ✅ | [PRs #6–#10](https://github.com/Moeez-rashid/student-task-manager/pulls?q=is%3Apr+is%3Amerged) |
| 1 resolved conflict | ✅ | merge commit "Merge branch status/testing" |
| ≥ 3 automated tests | ✅ 9 | `tests/test_task_manager.py` |
| 1 workflow (failed + successful run) | ✅ | [Actions](https://github.com/Moeez-rashid/student-task-manager/actions) |
| 1 release | ✅ | [v1.0.0](https://github.com/Moeez-rashid/student-task-manager/releases/tag/v1.0.0) |

Screenshots of every step are in [`lab-evidence/`](lab-evidence/).
