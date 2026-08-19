# Lab 12: Generics and traits

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs` and implement every `todo!()`. The `Stack<T>` struct and trait impl skeletons are already defined — make the pre-written tests pass. Do not modify the test module.

When implementing a method, rename parameters by dropping the leading `_`.

## What to implement

**`Stack<T>` methods**

| Method | Description |
|--------|-------------|
| `new()` | Return an empty stack backed by `Vec<T>` |
| `push(item)` | Append `item` to the top |
| `pop()` | Remove and return `Some(T)` from the top, or `None` if empty |
| `peek()` | Return `Some(&T)` to the top item without removing it, or `None` |
| `is_empty()` | `true` if the stack has no items |
| `len()` | Number of items |

**Trait impls**

| Impl | Description |
|------|-------------|
| `Display for Stack<T>` | Format as `[bottom, ..., top]`; empty stack as `[]` |

## Test locally

Run these from the `week12` directory:

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
git add week12/
git commit -m "Complete Lab 12"
git push origin main
```

A green Week 12 badge earns 10 points.
