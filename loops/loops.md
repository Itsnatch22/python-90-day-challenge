# Python Loops Guide

Loops in Python allow you to execute a block of code repeatedly. Python supports two main types of loops: `for` loops and `while` loops, along with loop control statements like `break`, `continue`, and `else`.

## 1. For Loops

The `for` loop is used for iterating over a sequence (like a list, tuple, string, or range).

### Basic Syntax
```python
for item in sequence:
    # Code block
    pass
```

### Examples

#### Iterating over a list
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
# Output:
# apple
# banana
# cherry
```

#### Using `range()`
```python
for i in range(5):  # 0 to 4
    print(i)
# Output: 0 1 2 3 4
```

```python
for i in range(2, 5):  # 2 to 4
    print(i)
# Output: 2 3 4
```

```python
for i in range(0, 10, 2):  # Start, end, step
    print(i)
# Output: 0 2 4 6 8
```

#### Iterating over a string
```python
for char in "hello":
    print(char)
# Output:
# h
# e
# l
# l
# o
```

#### Using `enumerate()` for index and value
```python
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")
# Output:
# 0: apple
# 1: banana
# 2: cherry
```

#### Using `zip()` to iterate over multiple sequences
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

## 2. While Loops

The `while` loop executes as long as the condition is `True`.

### Basic Syntax
```python
while condition:
    # Code block
    pass
```

### Examples

#### Simple counter
```python
count = 0
while count < 5:
    print(count)
    count += 1
# Output: 0 1 2 3 4
```

#### User input validation
```python
user_input = ""
while user_input != "exit":
    user_input = input("Enter 'exit' to quit: ")
    print(f"You entered: {user_input}")
```

## 3. Loop Control Statements

### `break` - Exit the loop
```python
for i in range(10):
    if i == 5:
        break
    print(i)
# Output: 0 1 2 3 4
```

### `continue` - Skip current iteration
```python
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Output: 1 3 5 7 9 (odd numbers only)
```

### `else` with loops (executes when no `break` occurs)
```python
for i in range(5):
    print(i)
else:
    print("Loop completed normally")

# With break:
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This won't print")
# Output: 0 1 2
```

## 4. Nested Loops

Loops inside loops:
```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

## 5. List Comprehensions (Loop Alternative)

Concise way to create lists:
```python
# Traditional for loop
squares = []
for i in range(5):
    squares.append(i**2)
print(squares)  # [0, 1, 4, 9, 16]

# List comprehension
squares = [i**2 for i in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# With condition
even_squares = [i**2 for i in range(10) if i % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]
```

## 6. Common Patterns

### Sum of numbers
```python
total = 0
for i in range(1, 101):
    total += i
print(f"Sum: {total}")  # Sum: 5050
```

### Finding maximum
```python
numbers = [3, 7, 2, 9, 1]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f"Max: {max_num}")  # Max: 9
```

### Infinite loop (avoid!)
```python
# DANGEROUS - Never do this without break condition!
# while True:
#     print("Infinite loop!")
```

## 7. Best Practices

1. **Use `for` loops** when iterating over known sequences
2. **Use `while` loops** when the number of iterations is unknown
3. **Prefer list comprehensions** for simple transformations
4. **Always update loop variables** in `while` loops to avoid infinite loops
5. **Use descriptive variable names**
6. **Avoid `else` with loops** unless necessary (can be confusing)

## Quick Reference Table

| Loop Type | When to Use | Example |
|-----------|-------------|---------|
| `for` | Known sequence length | `for item in list:` |
| `while` | Condition-based | `while count < 10:` |
| List Comp | List creation | `[x*2 for x in range(5)]` |

This covers everything essential about Python loops! Practice with these examples to master looping concepts.

