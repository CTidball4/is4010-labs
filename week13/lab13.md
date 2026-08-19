# Lab 13: Idiomatic Rust

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs` and implement every `todo!()`. The test suite is pre-written — make it pass. Do not modify the test module.

When implementing a function, rename parameters by dropping the leading `_`.

## What to implement

**Part 1 — Iterators and closures**

| Function | Description |
|----------|-------------|
| `analyze_text(text)` | Return `(word_count, avg_word_length, longest_word)`; use iterator adaptors |
| `process_numbers(numbers)` | Sum of squares of all even numbers: `[1,2,3,4]` → `4+16 = 20` |
| `make_counter()` | Return a closure (`impl FnMut() -> i32`) that increments on each call |

For `make_counter`: the closure wrapper is already in place — rename `_count` → `count`, increment it, and return the new value.

**Part 2 — Error handling with `Result`**

| Function / type | Description |
|-----------------|-------------|
| `divide(a, b)` | `Ok(a / b)` or `Err("division by zero")` when `b == 0.0` |
| `Display for ParseError` | Both variants must produce a non-empty message |
| `parse_positive_number(input)` | Parse `input` as `i32 > 0`; return `ParseError::NotANumber` or `ParseError::NotPositive` on failure |

## Test locally

Run these from the `week13` directory:

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

`cargo test` and `cargo clippy` both print the file, the line, and the reason. That is exactly
the context a coding agent needs. Paste the full output into Copilot CLI or Antigravity CLI and
ask it to explain the failure and show the idiomatic fix. Ask what the compiler or lint is
objecting to and why, not merely to make the check pass, and make sure you can explain the
change before you commit it.

## Submit

```bash
git add week13/
git commit -m "Complete Lab 13"
git push origin main
```

A green Week 13 badge earns 10 points.
