# Python Variables Guide

Variables in Python are used to store data values. Unlike many languages, Python doesn't require type declaration - the type is determined dynamically.

## 1. Creating Variables

**Syntax:** `variable_name = value`

### Rules for variable names:
- Must start with a letter or underscore `_`
- Can contain letters, numbers, underscores
- Case-sensitive (`age` ≠ `Age`)
- Avoid Python keywords (if, for, while, etc.)

### Examples
```python
# Integer
age = 25

# Float
height = 5.9

# String
name = "Alice"

# Boolean
is_student = True

# None (null equivalent)
score = None
```

## 2. Multiple Assignment

```python
# Same value to multiple variables
x = y = z = 0

# Different values to multiple variables
name, age, city = "Bob", 30, "New York"
print(name, age, city)  # Bob 30 New York
```

## 3. Data Types

| Type | Description | Example |
|------|-------------|---------|
| `int` | Whole numbers | `42`, `-10` |
| `float` | Decimal numbers | `3.14`, `2.0` |
| `str` | Text | `"hello"`, `'world'` |
| `bool` | True/False | `True`, `False` |
| `list` | Ordered, mutable | `[1, 2, 3]` |
| `tuple` | Ordered, immutable | `(1, 2, 3)` |
| `dict` | Key-value pairs | `{"name": "Alice"}` |
| `set` | Unique, unordered | `{1, 2, 3}` |

### Type checking and conversion
```python
age = 25
print(type(age))  # <class 'int'>

# Convert types
age_str = str(age)      # "25"
age_float = float(age)  # 25.0
age_int = int("30")     # 30
```

## 4. Dynamic Typing

```python
x = 10      # x is int
x = "hello" # x is now str
x = [1, 2]  # x is now list
```

## 5. Variable Scope

### Local scope (inside functions)
```python
def my_function():
    local_var = "I'm local"
    print(local_var)

my_function()  # Works
# print(local_var)  # Error! Not accessible outside function
```

### Global scope
```python
global_var = "I'm global"

def my_function():
    print(global_var)  # Can access global

my_function()
```

**Using `global` keyword to modify global variables:**
```python
counter = 0
def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1
```

### Nonlocal (nested functions)
```python
def outer():
    x = "outer"
    def inner():
        nonlocal x
        x = "inner"
    inner()
    print(x)  # inner

outer()
```

## 6. Common Patterns

### Swapping variables (Python way)
```python
a, b = 1, 2
print(a, b)  # 1 2

a, b = b, a  # No temp variable needed!
print(a, b)  # 2 1
```

### Default values
```python
name = input("Enter name: ") or "Anonymous"
print(name)
```

### Constants (by convention)
```python
PI = 3.14159
MAX_USERS = 100
# Don't change these!
```

## 7. Memory and References

### Mutable vs Immutable
```python
# Immutable (int, str, tuple) - Changes create new objects
x = 5
y = x
x = 10
print(y)  # Still 5

# Mutable (list, dict) - Changes affect all references
list1 = [1, 2, 3]
list2 = list1
list1.append(4)
print(list2)  # [1, 2, 3, 4]
```

### Copying lists
```python
import copy

original = [1, 2, 3]
shallow_copy = original.copy()     # or original[:]
deep_copy = copy.deepcopy(original)

original.append(4)
print(shallow_copy)  # [1, 2, 3] ✓
print(original)      # [1, 2, 3, 4]
```

## 8. Type Hints (Python 3.5+)

**Optional static typing for better code:**
```python
def greet(name: str, age: int) -> str:
    return f"Hello {name}, you are {age}!"

# IDEs use this for autocompletion and error checking
```

## 9. Best Practices

1. **Use descriptive names:**
   ```python
   # Good
   total_price = 99.99
   user_count = 42
   
   # Avoid
   x = 99.99
   n = 42
   ```

2. **Don't prefix with type** (`str_name`, `int_age`)
3. **Use snake_case** for variables
4. **Initialize before use**
5. **Avoid global variables** when possible
6. **Use `None` for uninitialized** instead of magic values

## 10. Debugging Variables

```python
# Print variable info
x = 42
print(f"x = {x}, type = {type(x)}")

# Debug with assert
assert x > 0, f"x must be positive, got {x}"
```

## Quick Reference Table

| Concept | Example | Notes |
|---------|---------|-------|
| Assignment | `x = 5` | Dynamic typing |
| Multiple | `a, b = 1, 2` | Unpacking |
| Scope | Local > Global | LEGB rule |
| Mutable | Lists, dicts | Shared references |
| Immutable | ints, strs, tuples | New objects on change |
| Constants | `MAX_SIZE = 100` | UPPERCASE by convention |

## Common Errors

1. **NameError:** Variable not defined
   ```python
   print(undefined_var)  # NameError
   ```

2. **UnboundLocalError:** Modifying global without `global`
3. **TypeError:** Wrong type for operation

This covers everything essential about Python variables!

