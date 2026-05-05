# Project-Local Operating Rules

This file defines repository-local operating rules for Codex work in this repository.

## Commit and Push Sync Rule

When a substantial work block is completed, Codex should proactively recommend a Git checkpoint.

A substantial work block includes:
- any completed implementation patch;
- multi-file documentation or instruction updates;
- project-memory/session recap updates;
- validation evidence updates;
- GitHub/repository setup changes;
- any task where losing local state would be costly;
- end-of-session or context-switch moments after meaningful changes.

Codex must not silently commit or push.

Before proposing commit + push, Codex must check:
1. `git status -sb`
2. changed files / diff summary
3. whether relevant validation/checks were run or explicitly skipped
4. whether secrets or obviously local/private artifacts are being added
5. whether the repository has a configured GitHub remote/upstream

Codex should then ask the user in clear terms, for example:
"Работа завершена и repo изменён. Рекомендую сделать commit + push в GitHub. Сделать сейчас?"

If the user explicitly agrees, Codex should:
1. show final `git status -sb`
2. stage only intended files
3. create a clear commit message
4. run `git commit`
5. run `git push`
6. show final `git status -sb`
7. show the latest commit hash and remote branch

If the repository has no remote/upstream, Codex must stop and report that push is not configured.

If there are unrelated changes, Codex must not stage them blindly. It must either exclude them or ask the user.

If validation was not run, Codex must say that clearly in the commit/push proposal.
