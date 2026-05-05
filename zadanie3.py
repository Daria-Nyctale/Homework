name = input ("You name?")  
age = input("your age?")

#print("", (name),(age))

try:
    age = int(age)
    print(f"ваше имя и возраст: {name}, {age}")   
    
    with open("user_data.txt","a", encoding="utf-8") as my_file:
        print("ваше имя и возраст: {}, {}".format(name, age), file=my_file)
        print(f" {type(name)},{type(age)}",file=my_file)
        print("данные для проверки",file=my_file)
        print("Все данные сохранены")
except ValueError:                          
    print("error:ввеедите число")




    



