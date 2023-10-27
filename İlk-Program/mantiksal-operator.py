## Mantıksal Operatörler (Logical Operators)

# not 
print(not True)    # --> false
print(not False)   # --> true
print(not 5 < 6)   # --> false
print(not 5 == 5)  # --> false

a = 4
b = 10
print(not a < b)   # --> false
print(not (a > b)) # --> true



# and
# Sadece iki ifade de True ise True sonucu verir, yoksa False olur.
print(True and True)    # --> true
print(True and False)   # --> false
print(False and False)  # --> false

a = 4
b = 1
c = 10
print((a > b) and (b < c))   # --> true
print((a > b) and (b > c))   # --> false



# or
# Sadece iki ifade de False ise False sonucu verir, yoksa True olur.
print(True or True)    # --> true
print(True or False)   # --> true
print(False or False)  # --> false

a = 4
b = 1
c = 10
print((a > b) or (b < c))   # --> true
print((a > b) or (b > c))   # --> true
print((a < b) or (b > c))   # --> false


# Short-circuit
print("sonuç :",(5 < 3) and print("hey"))   # --> false
print("sonuç :",(5 > 3) or print("hey"))    # --> true
print("sonuç :",(5 < 3) or print("hey"))    # --> hey
print("sonuç :",(5 > 3) and print("hey"))   # --> hey