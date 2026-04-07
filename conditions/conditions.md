# Python Conditions Guide

Conditional statements in Python (often called "if statements") allow you to execute different code blocks based on whether a condition is true or false. Python uses `if`, `elif`, and `else` keywords.

## 1. Basic If Statement

### Syntax
```python
if condition:
    # Code block if condition is True
    pass
```

### Example
```python
age = 18
if age >= 18:
    print("You are an adult!")
# Output: You are an adult!
```

## 2. If-Else Statement

### Syntax
```python
if condition:
    # Code block if True
else:
    # Code block if False
```

### Example
```python
age = 16
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor!")
# Output: You are a minor!
```

## 3. If-Elif-Else Chain

### Syntax
```python
if condition1:
    # Code for condition1
elif condition2:
    # Code for condition2
elif condition3:
    # Code for condition3
else:
    # Default code
```

### Example - Grade system
```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
# Output: Grade: B
```

## 4. Comparison Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `==` | Equal | `x == 5` |
| `!=` | Not equal | `x != 5` |
| `>` | Greater than | `x > 5` |
| `<` | Less than | `x < 5` |
| `>=` | Greater or equal | `x >= 5` |
| `<=` | Less or equal | `x <= 5` |

## 5. Logical Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `and` | True if both are True | `x > 5 and x < 10` |
| `or` | True if either is True | `x == 5 or x == 10` |
| `not` | Inverts the truth value | `not(x == 5)` |

### Examples
```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
# Output: You can drive!
```

```python
temperature = 30
is_raining = False

if temperature > 25 or is_raining:
    print("Stay hydrated!")
# Output: Stay hydrated!
```

## 6. Membership Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `in` | Value is in sequence | `"a" in "apple"` |
| `not in` | Value is not in sequence | `"b" not in "apple"` |

### Example
```python
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Found banana!")
# Output: Found banana!
```

## 7. Identity Operators

| Operator | Description | Example |
|----------|-------------|---------|
| `is` | Same object | `x is y` |
| `is not` | Not same object | `x is not y` |

## 8. Nested Conditions

```python
score = 85
attendance = 90

if score >= 80:
    if attendance >= 75:
        print("Pass with honors!")
    else:
        print("Pass")
else:
    print("Fail")
# Output: Pass with honors!
```

**Alternative with `and`** (cleaner):
```python
if score >= 80 and attendance >= 75:
    print("Pass with honors!")
elif score >= 80:
    print("Pass")
else:
    print("Fail")
```

## 9. Ternary Operator (Conditional Expression)

**Syntax:** `value_if_true if condition else value_if_false`

### Example
```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # Output: adult
```

```python
numbers = [1, 2, 3, 4, 5]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4]
```

## 10. Common Patterns

### Positive/Negative check
```python
number = -5
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")
```

### Even/Odd check
```python
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")
# Output: Odd
```

### Validating user input
```python
user_input = input("Enter a number: ")
if user_input.isdigit():
    num = int(user_input)
    print(f"You entered: {num}")
else:
    print("Invalid input!")
```

## 11. Truthiness

In Python, certain values are considered "falsy":
- `False`
- `None`
- `0`, `0.0`
- `""` (empty string)
- `[]`, `{}`, `()` (empty collections)
- Everything else is "truthy"

### Example
```python
name = ""
if name:  # Same as if name != ""
    print("Hello, " + name)
else:
    print("No name provided")
# Output: No name provided
```

## 12. Best Practices

1. **Avoid deep nesting** - Use `and`/`or` instead of nested ifs
2. **Use early returns** in functions when possible
3. **Be explicit** with comparisons (prefer `!= None` over `is not None`)
4. **Use descriptive conditions**
5. **Consider using dictionaries** for multiple conditions:
   ```python
   grades = {90: 'A', 80: 'B', 70: 'C', 60: 'D'}
   score = 85
   grade = 'F'
   for threshold, letter in grades.items():
       if score >= threshold:
           grade = letter
           break
   print(f"Grade: {grade}")  # Grade: B
   ```

## Quick Reference Table

| Statement | Purpose | Example |
|-----------|---------|---------|
| `if` | Single condition | `if x > 0:` |
| `if-else` | Two possibilities | `if x > 0: ... else: ...` |
| `if-elif-else` | Multiple conditions | `if x > 0: elif x < 0: else:` |
| Ternary | One-liner | `x if cond else y` |
| `in` | Membership | `if item in list:` |

This guide covers all essential Python conditional statements and patterns!

