# IS4010 labs

This repository contains all 14 labs for **IS4010: AI-enhanced application development**. Labs 01–08 use the Python development environment; Labs 09–14 use Rust.

> [!WARNING]
> Work only in the files identified by each lab. Do not modify this README, lab instructions, tests, or anything under `.github/`. Those files control automated grading.

## Lab status

A green badge on your fork's `main` branch means the corresponding lab is complete and earns **10 points**.

| Lab | Topic | Status |
|---:|---|:---:|
| 01 | Repository and development setup | [![Week 01](../../actions/workflows/week01.yml/badge.svg?branch=main)](../../actions/workflows/week01.yml) |
| 02 | Compare CLI coding agents | [![Week 02](../../actions/workflows/week02.yml/badge.svg?branch=main)](../../actions/workflows/week02.yml) |
| 03 | Python basics and automated testing | [![Week 03](../../actions/workflows/week03.yml/badge.svg?branch=main)](../../actions/workflows/week03.yml) |
| 04 | Data structures | [![Week 04](../../actions/workflows/week04.yml/badge.svg?branch=main)](../../actions/workflows/week04.yml) |
| 05 | Functions and error handling | [![Week 05](../../actions/workflows/week05.yml/badge.svg?branch=main)](../../actions/workflows/week05.yml) |
| 06 | Object-oriented programming | [![Week 06](../../actions/workflows/week06.yml/badge.svg?branch=main)](../../actions/workflows/week06.yml) |
| 07 | External data and APIs | [![Week 07](../../actions/workflows/week07.yml/badge.svg?branch=main)](../../actions/workflows/week07.yml) |
| 08 | Weather CLI application | [![Week 08](../../actions/workflows/week08.yml/badge.svg?branch=main)](../../actions/workflows/week08.yml) |
| 09 | Rust basics | [![Week 09](../../actions/workflows/week09.yml/badge.svg?branch=main)](../../actions/workflows/week09.yml) |
| 10 | Ownership and borrowing | [![Week 10](../../actions/workflows/week10.yml/badge.svg?branch=main)](../../actions/workflows/week10.yml) |
| 11 | Structs, enums, and methods | [![Week 11](../../actions/workflows/week11.yml/badge.svg?branch=main)](../../actions/workflows/week11.yml) |
| 12 | Generics and traits | [![Week 12](../../actions/workflows/week12.yml/badge.svg?branch=main)](../../actions/workflows/week12.yml) |
| 13 | Idiomatic Rust | [![Week 13](../../actions/workflows/week13.yml/badge.svg?branch=main)](../../actions/workflows/week13.yml) |
| 14 | CLI application | [![Week 14](../../actions/workflows/week14.yml/badge.svg?branch=main)](../../actions/workflows/week14.yml) |

## Start here

Complete [Lab 01](week01/lab01.md). It walks you through the terminal, forking this repository, cloning your fork, enabling GitHub Actions, and preparing Python with `uv` for the first half of the course.

GitHub disables workflows in a new public fork until its owner enables them. Open the **Actions** tab in your fork and select **I understand my workflows, go ahead and enable them** before pushing your Lab 01 setup record.

## Weekly workflow

1. Read `weekXX/labXX.md`.
2. Work only in the files the lab identifies.
3. Run the week's tests locally.
4. Commit and push to your fork's `main` branch.
5. Confirm that the corresponding badge above is green.

Start a Python lab with `uv sync --locked`, then run its documented `uv run python -m pytest` command. Rust labs use `cargo test`, `cargo fmt --check`, and `cargo clippy -- -D warnings`.
