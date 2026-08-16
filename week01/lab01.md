# Lab 01: Repository and development setup

**Due:** Sunday at 11:59 PM  
**Points:** 10

This lab prepares the single repository you will use for every lab in the course. You will fork it, clone your fork, prepare Python, enable GitHub Actions, and push a short setup record. Rust is already included for later in the semester; you will install its toolchain before Week 09.

## Learning objectives

By the end of this lab, you will be able to:

- Explain the difference between a repository, fork, and clone
- Configure Git with your identity
- Fork and clone a GitHub repository
- Verify that your local `origin` points to your fork
- Create a Python virtual environment
- Enable and inspect GitHub Actions
- Commit and push a change to GitHub

## 1. Install the Week 01 tools

Follow the course [setup guide](https://bgreenwell.github.io/is4010-website/resources/setup.html) to install:

- Visual Studio Code
- Git
- Python 3.10 or newer

Verify them in a terminal:

```bash
code --version
git --version
python --version
```

On systems where `python` is unavailable, try `python3`.

## 2. Configure Git

```bash
git config --global user.name "Your name"
git config --global user.email "your-email@example.com"
git config --global --list
```

Use the email associated with your GitHub account. Follow GitHub's current authentication instructions when prompted; never paste a token into a file or commit it.

## 3. Fork the semester repository

1. Open <https://github.com/bgreenwell/is4010-labs>.
2. Select **Fork**.
3. Keep the repository name `is4010-labs`.
4. Create the fork under your own GitHub account.

Your fork URL should look like:

```text
https://github.com/YOUR-USERNAME/is4010-labs
```

## 4. Clone your fork

```bash
mkdir -p ~/is4010
cd ~/is4010
git clone https://github.com/YOUR-USERNAME/is4010-labs.git
cd is4010-labs
git remote -v
```

Both `origin` lines must contain your GitHub username. If they point to `bgreenwell`, you cloned the course repository instead of your fork.

## 5. Prepare Python

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python --version
pytest --version
```

Windows PowerShell users activate with `.venv\Scripts\Activate.ps1`. Windows Git Bash users activate with `source .venv/Scripts/activate`.

## 6. Enable GitHub Actions

Open the **Actions** tab in your fork. If GitHub displays a warning that workflows are disabled, select **I understand my workflows, go ahead and enable them**.

## 7. Create your setup record

Copy the template and edit the copy:

```bash
cp week01/student_setup.template.md week01/student_setup.md
```

Replace every placeholder. Use the exact Python version printed by `python --version` and mark local clone verification as `yes`.

## 8. Commit and push

```bash
git add week01/student_setup.md
git commit -m "Complete Lab 01 setup"
git push origin main
```

Open your fork's README and wait for the Week 01 badge to turn green. Select the badge to inspect the workflow if it fails.

## Submit on Canvas

Submit this single URL:

```text
https://github.com/YOUR-USERNAME/is4010-labs
```

A green Week 01 badge earns 10 points.
