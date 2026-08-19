# Lab 09: Rust basics

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/main.rs` and implement every `todo!()`. The test suite is pre-written — make it pass. Do not modify the test module.

When implementing a function, rename parameters by dropping the leading `_` (e.g., `_a` → `a`).

## What to implement

| Function | Description |
|----------|-------------|
| `add(a, b)` | Return `a + b` |
| `multiply(a, b)` | Return `a * b` |
| `is_even(n)` | Return `true` if `n` is divisible by 2 |
| `max(a, b)` | Return the larger of the two values |
| `square(n)` | Return `n * n` |
| `reverse_string(s)` | Return the input string reversed |
| `concat_with_separator(words, sep)` | Join words with the given separator |
| `find_max_in_vec(numbers)` | Return the maximum value, or `None` if empty |
| `count_evens(numbers)` | Return the count of even numbers in the slice |

## Test locally

Run these from the `week09` directory:

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
git add week09/
git commit -m "Complete Lab 09"
git push origin main
```

A green Week 09 badge earns 10 points.
