# Lab 10: Ownership and borrowing

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs`. There are two parts.

**Part 1 — borrow-checker puzzles (not graded automatically):** Seven functions are commented out with `/* ... */`. Each has a compile error. Read the comment above each one, fix the broken code, then uncomment the call in `main()` to verify it runs.

**Part 2 — implementation exercises (graded):** Implement the four `pub` functions below. Remove the leading `_` from parameter names as you go. Do not modify the test module.

## What to implement (Part 2)

| Function | Signature | Description |
|----------|-----------|-------------|
| `to_uppercase_owned` | `(s: String) -> String` | Take ownership, convert to uppercase, return |
| `string_length` | `(s: &String) -> usize` | Borrow immutably, return length |
| `append_suffix` | `(s: &mut String, suffix: &str)` | Mutably borrow, append `suffix` in place |
| `concat_strings` | `(s1: &str, s2: &str) -> String` | Borrow two slices, return a new owned `String` |

## Test locally

Run these from the `week10` directory:

```bash
cargo test
cargo fmt
cargo clippy -- -D warnings
```

CI runs `cargo fmt --check`, so run `cargo fmt` before you push.

## If the style checks fail

`cargo test` checks that your code is **correct**. `cargo fmt` and `cargo clippy` check that it
is **idiomatic**, and CI runs both, so working code can still leave the badge red. This is not a
trick: formatting and lints are part of everyday Rust work.

Fix most of it automatically:

```bash
cargo clippy --fix --allow-dirty
cargo fmt
```

One common lint is **not** auto-fixable, and it comes straight from Python habits:

| Clippy says | Why | Rewrite |
|---|---|---|
| `the loop variable i is only used to index` | Rust iterates over items directly | `for n in numbers` instead of `for i in 0..numbers.len()` |

Read the message clippy prints; it names the file, the line, and the idiom. Re-run all three
commands before you push.

## Submit

```bash
git add week10/
git commit -m "Complete Lab 10"
git push origin main
```

A green Week 10 badge earns 10 points.
