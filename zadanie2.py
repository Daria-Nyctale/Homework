
number_1 = input("enter number:") 
number_2 = input("enter number2:")

print(f" {type(number_1)}, {type(number_2)}") 
 

try:
    number_1 = int(number_1)
    number_2 = int(number_2)

    print(f" {type(number_1)}, {type(number_2)}") 

    sum_numbers = number_1 + number_2
    dif_numbers = number_1 - number_2
    mult_numbers = number_1 * number_2

    print(f"sum: {sum_numbers}") 
    print("difference:",(dif_numbers))
    print("multiplication: {}" .format(mult_numbers))
    print("results:", sum_numbers, dif_numbers, mult_numbers, sep=" ", end="\n")
except:
    print("Incorrect data entered")


 






