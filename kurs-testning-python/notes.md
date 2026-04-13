# Exercise 19 Notes

## What Exercise 19 Was About

Build one local pipeline and one GitHub pipeline for an existing Python exercise.
The pipeline should automatically:

- check code style with `flake8`
- run tests with `pytest`
- show coverage
- stop on failure

Think of it like this:

```text
code
 |
 v
style check
 |
 v
tests
 |
 v
coverage
 |
 v
pass/fail
```

## Local Bash Version

Use an existing exercise, like `ovningar/05`.

The script idea:

- use Bash
- stop on first error with `set -e`
- run `flake8`
- run `pytest` with coverage
- print simple messages so you can follow what is happening

Typical flow:

```sh
cd /app/ovningar/05
chmod +x run_pipeline.sh
./run_pipeline.sh
```

Important idea:
The script works relative to the folder you run it from.

If you are in `ovningar/05`, then short file names like `calculator.py` work.

## Container Notes

From the repo's `container/` folder:

```sh
podman build -t testing .
podman run -it --rm -v ..:/app --name testlab testing
```

Then inside the container:

```sh
cd /app/ovningar/05
./run_pipeline.sh
```

Important mistake to remember:
`podman build -t testing` is missing the final dot.
Correct command is:

```sh
podman build -t testing .
```

The dot means:
use this folder as the build context.

## GitHub Actions Version

The GitHub workflow does the same thing as the Bash script, but runs automatically on push.

Important idea:
Bash script = you press the button
GitHub Actions = GitHub presses the button when you push

## Where the workflow file must go

This was the biggest trap.

GitHub only reads workflow files from the repo root:

```text
.github/workflows/tests.yml
```

That is:

- `.github` = folder
- `workflows` = folder inside `.github`
- `tests.yml` = file inside `workflows`

If the file is inside a subfolder project, GitHub ignores it.

Wrong:

```text
repo/kurs-testning-python/.github/workflows/tests.yml
```

Right:

```text
repo/.github/workflows/tests.yml
```

## Why the paths changed

When the workflow moved to the repo root, GitHub started from the repo root too.

So instead of:

```yaml
working-directory: ovningar/05
```

it had to become:

```yaml
working-directory: kurs-testning-python/ovningar/05
```

because `kurs-testning-python` was a folder inside the actual repo.

Main lesson:
Always ask:
"From the GitHub repo root, where are my files?"

## Basic Workflow Structure

A workflow file answers these questions:

- what is it called?
- when should it run?
- what machine runs it?
- what steps should happen?

Main blocks:

- `name:` = workflow title
- `on:` = trigger, like `push`
- `jobs:` = the work to do
- `runs-on:` = machine, usually `ubuntu-latest`
- `steps:` = ordered actions
- `uses:` = GitHub helper action
- `run:` = shell command
- `working-directory:` = which folder the command runs from

## Mental Model for GitHub Actions

GitHub does this:

```text
push happens
 |
 v
create fresh Ubuntu machine
 |
 v
checkout repo
 |
 v
set up Python
 |
 v
install tools
 |
 v
go to the right folder
 |
 v
run flake8
 |
 v
run pytest with coverage
 |
 v
pass/fail
```

## Typical Workflow Shape

The logic you used was:

- checkout code
- set up Python
- install `flake8`, `pytest`, `pytest-cov`
- run `flake8`
- run `pytest` with coverage

## Common Mistakes to Watch For

- wrong folder for workflow file
- missing spaces in YAML like `uses: actions/...`
- forgetting that GitHub starts from repo root
- forgetting to install dependencies in GitHub
- wrong filenames
- typo in command flags
- forgetting the `.` in `podman build -t testing .`

## Git Ignore Notes

Generated files should not usually be committed:

- `.coverage`
- `.pytest_cache/`
- `__pycache__/`
- `*.pyc`

But assignment files should be committed:

- `run_pipeline.sh`
- `.github/workflows/tests.yml`
- `.gitignore`

Important lesson:
`.gitignore` does not automatically untrack files already tracked by git.

## Safer Git Habit

Instead of `git add -A`, stage only the files you actually want:

```sh
git add .github/workflows/tests.yml .gitignore ovningar/05/run_pipeline.sh
```

That keeps junk out of the commit.

## How to Tell If GitHub Actions Is Working

Go to the `Actions` tab.

Working means:

- you see your workflow name
- you see runs triggered by push
- green check = passed
- red X = failed

A failed run still proves something important:
GitHub found and ran the workflow.

## Simple Reusable Checklist

When doing this again on another project:

1. Pick the project files and test files.
2. Make the local Bash script work first.
3. Confirm `flake8` works.
4. Confirm `pytest` with coverage works.
5. Put workflow file in repo root `.github/workflows/`.
6. Remember GitHub starts from repo root.
7. Fix paths with `working-directory` or full paths.
8. Install tools in the workflow.
9. Commit and push.
10. Check the `Actions` tab.

## One Sentence Summary

Exercise 19 is about taking test commands that already work locally and teaching GitHub to run them automatically on every push.
