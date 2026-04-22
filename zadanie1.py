name = input ("You name?")
age = int(input ("your age?"))
number = bool(input ("favorite number?")) 

print(f" {name}, {age}, {number}")

print("Type:",type(name),type(age),type(number))

multi_line_str = '''name,
 age,
 number'''
print(multi_line_str)

path = r"D:\repose\hello\zadanie1.txt"
print(path)
