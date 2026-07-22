# No declarations — type inferred from value
i = 42                  # int (arbitrary precision, no int/long distinction)
f = 3.14                # float (Java's double)
c = 3 + 4j               # complex number — no Java equivalent
s = "hello"              # str (single or double quotes both fine)
b = True                 # bool (capital T/F, not true/false)
n = None                 # Java's null

print(type(i), type(f), type(s), type(b))  # <class 'int'> etc.

# Type conversion (Java's casting)
x = int("42")
y = float("3.14")
z = str(100)
w = bool(0)  # False — 0, "", [], None, {} are all falsy
