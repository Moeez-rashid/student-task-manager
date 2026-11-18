# Lab evidence

Screenshots of the key steps, in the order they were done.

| # | Screenshot | Part | Shows |
|---|---|---|---|
| 01 | [repository-home](01-repository-home.png) | A | Public repo with README, MIT license, Python `.gitignore` |
| 02 | [git-config](02-git-config.png) | A | `git config` user name/email after cloning, remote |
| 03 | [status-add-commit-diff](03-status-add-commit-diff.png) | A | `git status`, `git add`, `git commit`, `git diff` |
| 04 | [status-diff-gitignore](04-status-diff-gitignore.png) | A | `git status`, `git diff --stat`, ignoring `tasks.json` |
| 05 | [push-pull](05-push-pull.png) | A | `git log`, `git push`, `git pull` of a change made on GitHub |
| 06 | [branches-compare](06-branches-compare.png) | B | All branches; comparing each feature branch with `main` |
| 07 | [commit-graph](07-commit-graph.png) | B | `git log --graph --all` — three feature branches from one commit |
| 08 | [branches-on-github](08-branches-on-github.png) | B | Branches pushed to GitHub |
| 09 | [issues-with-labels](09-issues-with-labels.png) | C | Five labelled Issues, closed by their PRs |
| 10 | [pr-review-comment](10-pr-review-comment.png) | C | PR #6 linked to Issue #1, inline review comment, merged |
| 22 | [pr-files-changed](22-pr-files-changed.png) | C | Files changed view of PR #6 |
| 11 | [merged-pull-requests](11-merged-pull-requests.png) | C/H | Five merged Pull Requests (#6–#10) |
| 12 | [conflict-setup](12-conflict-setup.png) | D | "Project status: Planning" on main, two branches from that commit |
| 13 | [conflict-before-resolution](13-conflict-before-resolution.png) | D | First merge OK, second merge → CONFLICT, conflict markers |
| 14 | [conflict-after-resolution](14-conflict-after-resolution.png) | D | Resolved line, no markers left, merge committed and pushed |
| 15 | [commit-history](15-commit-history.png) | D/H | Commit history on GitHub incl. both merge commits |
| 16 | [actions-failed-and-successful-runs](16-actions-failed-and-successful-runs.png) | E | Workflow runs: one failed (Tests #1), the rest successful |
| 17 | [tests-local](17-tests-local.png) | E | `python -m unittest discover -s tests -v` locally — 9 tests OK |
| 18 | [actions-failed-run](18-actions-failed-run.png) + [log](18b-actions-failed-run-log.png) | E | Failed run: `test_delete_task` FAIL |
| 19 | [actions-successful-run](19-actions-successful-run.png) + [log](19b-actions-successful-run-log.png) | E | Successful run after the fix: 9 tests OK |
| 20 | [app-demo](20-app-demo.png) | A/B | The console app: add, empty-title error, display, complete `1,3`, delete with validation + confirmation |
| 21 | [release-v1.0.0](21-release-v1.0.0.png) | F | Published GitHub Release `v1.0.0` with release notes |

Terminal screenshots are rendered from the real command output captured while doing each step; GitHub screenshots are of the live public pages.
