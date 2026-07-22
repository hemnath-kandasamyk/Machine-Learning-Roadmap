a, b = 17, 5
print(a // b)   # 3   — floor division (Java's / for ints)
print(a % b)    # 2   — modulo, same as Java
print(a ** b)   # 1419857 — exponentiation, no Math.pow needed

# Chained comparisons — no Java equivalent
x = 5
print(1 < x < 10)  # True, same as (1 < x && x < 10)

# Logical operators are words, not symbols
print(True and False, True or False, not True)  # &&, ||, ! in Java
