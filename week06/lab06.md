# Lab 06: Object-oriented programming

**Due:** Sunday at 11:59 PM  
**Points:** 10

Model printed and electronic books with classes, inheritance, constructors, and string representations.

## Deliverable

Create `week06/lab06.py`. Do not copy or modify the provided tests.

## `Book`

Implement a `Book` class whose constructor stores:

- `title`
- `author`
- `year`

Its `__str__` result must include all three values. Add:

```python
def get_age(self):
    """Return 2026 minus the publication year."""
```

Use 2026 consistently so the automated result is deterministic.

## `EBook`

Implement `EBook` as a subclass of `Book`. Its constructor accepts the three book values plus `file_size` in megabytes. Reuse the parent constructor with `super()`.

Its `__str__` result must include the inherited book information, file size, and the text `MB`. It must inherit `get_age` without duplicating that method.

## Test locally

```bash
PYTHONPATH=week06 pytest week06/tests/ -v
```

## Submit

```bash
git add week06/lab06.py
git commit -m "Complete Lab 06"
git push origin main
```

A green Week 06 badge earns 10 points.

