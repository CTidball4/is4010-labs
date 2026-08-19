# Lab 11: Structs, enums, and methods

**Due:** Sunday at 11:59 PM  
**Points:** 10

Open `src/student.rs` and implement every `todo!()`. The types (`Student`, `Grade`, `CourseGrade`, `StudentDatabase`) are already defined — do not change them. The test suite is pre-written — make it pass. Do not modify the test module.

When implementing a method, rename parameters by dropping the leading `_` (e.g., `_id` → `id`).

## What to implement

**`Student`**

| Method | Description |
|--------|-------------|
| `new(id, name, email)` | `credits_earned` starts at 0, `grades` starts empty |
| `class_standing()` | `"Freshman"` 0–29 cr, `"Sophomore"` 30–59, `"Junior"` 60–89, `"Senior"` 90+ |
| `add_credits(credits)` | Add to `credits_earned` |
| `can_graduate()` | `true` if `credits_earned >= 120` |
| `add_grade(course_grade)` | Append to `grades` |
| `calculate_gpa()` | Weighted GPA = total quality points / total credit hours; `0.0` if no grades |

**`Grade`**

| Method | Description |
|--------|-------------|
| `to_gpa_points()` | `A→4.0`, `B→3.0`, `C→2.0`, `D→1.0`, `F→0.0` |
| `from_string(s)` | Parse `"A"`–`"F"` (case-insensitive); `None` for anything else |
| `is_passing()` | `true` for A, B, C |

**`CourseGrade`**

| Method | Description |
|--------|-------------|
| `new(course_code, course_name, credits, grade)` | Construct a `CourseGrade` |
| `quality_points()` | `credits as f32 × grade.to_gpa_points()` |

**`StudentDatabase`**

| Method | Description |
|--------|-------------|
| `new()` | Empty database (uses `HashMap`) |
| `add_student(student)` | Add by id; return `Err(String)` if id already exists |
| `find_student(id)` | `Option<&Student>` |
| `find_student_mut(id)` | `Option<&mut Student>` |
| `student_count()` | Number of students |
| `average_gpa()` | Mean GPA across all students; `0.0` if empty |
| `list_students()` | `Vec<&Student>` of all students |

## Test locally

Run these from the `week11` directory:

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
git add week11/
git commit -m "Complete Lab 11"
git push origin main
```

A green Week 11 badge earns 10 points.
