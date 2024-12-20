
from person import Person

#my_person = Person(name="Danny de Vet", age=56, gender="man", height=1.68, mass=65, occupation="fearless lion tamer", favourite_food="'gebakken stront'")

#print(my_person.walk())
#print(my_person.eat("'gebakken hond'"))
#print(my_person.sleep())
#print(my_person.work())
#print(my_person.introduce())


def print_menu():
    print("\n**************************")
    print("**      The Simz        **")
    print("**************************")
    print("**************************")
    print("*1.Create a character    *")
    print("*2.Exit                  *")
    print("**************************")
    print("*Character creation menu *")
    print("**************************")
while True:
    print_menu()
    keuze = input("Select an option (1-2):")
    if keuze == "1":
        print("\nCharacter Creation Menu")
        name = input("Enter your character's name: ")
        age = int(input("Enter your character's age: "))
        gender = input("Enter your character's gender (m/f/o): ")
        if gender=="m":
                gender =gender.replace("m","male")
        elif gender=="f":
                gender = gender.replace ("f", "female")
        elif gender =="o":
                gender= gender.replace ("o","omnigender")
        else:
            print("Incorrect gender, gender will be 'alien'")
            gender = "alien"
        height = float(input("Enter your character's height (meters): "))
        mass = float(input("Enter your character's mass (kg): "))
        occupation = input("Enter your character's occupation: ")
        favourite_food = input("Enter your character's favourite food: ")
        user_person = Person(name, age, gender, height, mass, occupation, favourite_food)
#        print(user_person.walk())
#        print(user_person.eat("'sjoekelat'"))
#        print(user_person.eat(favourite_food))
#        print(user_person.sleep())
#        print(user_person.work())
        print(user_person.introduce())
        break

    elif keuze == "2":
        print("\n     Thank you for using    ")
        print("     the Character Creation   ")
        print("******************************")
        print("*      Shutting down ...     *")
        print("******************************")
        break
    else:
        print("Invalid option")

