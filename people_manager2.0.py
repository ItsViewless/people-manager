import json


def load_people():
    try:
        with open("people.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
        
        
people = load_people()


def save_people():
    with open("people.json", "w") as file:
        json.dump(people, file, indent=4)


def add_person():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    
    person = {
        "name": name,
        "age": age
    }
    
    people.append(person)
    save_people()
    
    
def show_people():
    for person in people:
        print(person["name"], "-", person["age"])
        
        
def menu():
    while True:
        print("1 - Add person")
        print("2 - Show people")
        print("3 - Delete person")
        print("4 - Find person")
        print("5 - Statistics")
        print("6 - Show adults")
        print("q - Quit")
        
        choice = input("Choose: ")
        if choice == "1":
            add_person()
        elif choice == "2":
            show_people()
        elif choice == "3":
            delete_person()
        elif choice == "4":
            find_person()
        elif choice == "5":
            show_statistics()
        elif choice == "6":
            show_adults()
        elif choice == "q":
            break
        else:
            print("Unknown command!")


def delete_person():
    name = input("Enter name to delete: ")
    
    for person in people:
        if person["name"] == name:
            people.remove(person)
            save_people()
            print("Person deleted!")
            return
            
    print("Person not found!")
    

def find_person():
    name = input("Enter name to find: ")
    
    for person in people:
        if person["name"] == name:
            print(person["name"], "-", person["age"])
            print("Person found!")
            return
            
    print("Person not found!")
    
    
def show_statistics():
    count = len(people)
    total_age = 0
    
    for person in people:
        total_age = total_age + person["age"]
        
    print("Total people:", count)
    print("Total age:", total_age)
    
    if count > 0:
        average_age = total_age / count
        print("Average age:", average_age)
    else:
        print("No people yet.")
        
def show_adults():
    for person in people:
        if person["age"] >= 18:
            print(person["name"], "-", person["age"])

menu()

print("People Manager 2.0 - Git")