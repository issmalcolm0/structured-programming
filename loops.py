###

'''
## Syntax
for count in condition:
    logic

'''


## Example: Write a program to print fist 100,even numbers:
print("1")
print("2")
print("3")
print("4")
print("5")
print("6")
print("7")
print("8")
print("9")
print("10")
print("...")
print("100")

## for
for number in range(1,201):
    if number%2 == 0:
     print(number)
     pass

# option 2:
for number in range(0, 201, 2):
    print(number)    