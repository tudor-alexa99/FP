from operations import *

def print_commands():
    print(" 1.Add animal to the list:<code>, <name>, <type> , <species> ")
    print(" 2.Modify animal by code: ")
    print(" 3.List all animals: ")
    print(" 4.Show all <type> animals, sorted by <name>")
    print(" 5.Change <type> of animals by <species>")

def start(zooList):
    while True:
        print_commands()
        c = input("\n \t Insert command here: \n")
        if verify_c(c):
            process_command(c,zooList)
        elif c == "0":
            return
        else:
            print("please insert a valid command here!")



def process_command(c, zooList):
    #for each entry compute the operations
    if c == "1":
        create_animal = read_animal_UI()
        if create_animal != None:
            code, name, type, species = create_animal
            add_animal(zooList,code,name,type,species)
        else:
            print("Please inset non-void attributes to the animal")
    elif c == "2":
        #update an animal's type by code
        code = read_code()
        if code != None:
            new_type = insertType()#
            if new_type!= None:
                update_animal(zooList, code, new_type)
    elif c == "3":
        #prints the list
        printList(zooList)
        print("\n")
    elif c == "4":
        #sort the list of animal's types by the name
        type = insertType()
        print(sort_type(zooList, type))

    elif c == "5":
        new_species = insertSpecies()
        new_type = insertType()
        if new_type != None and new_species != None:
            change_type_by_species(zooList, new_type, new_species)
        else:
            print ("please insert non-void type and species!")

def read_animal_UI():
    try:
        #gets the user input
        code = int(input("\tInsert a code here: "))
        name = input("\tInsert a name here: ")
        type = input("\tInsert a type here: ")
        species = input("\tInsert a species here:")
        if code != None and len(name) != 0 and len(type) != 0 and len(species) != 0:
            return code, name, type, species
        else:
            return None
    except ValueError:
        print("Please insert a valid number on the id ")
        return None


def printList(zooList):
    for animal in zooList:
        print(animal)


def read_code():
    try:
        code = int(input("Inset new code here: "))
        #check if the code is in the list
        if search_for_code(zooList, code) == True:
            return code
        else:
            print("Please insert an existing code here!")
            return None
    except TypeError:
        print("Please insert a valid number as a code")


def insertType():
    type = input(("Insert type here: "))
    if len(type) == 0:
        print("Please insert a non-empty type")
        return None
    return type

def insertSpecies():
    species = input(("Insert species here: "))
    if len(species) == 0:
        print("Please insert a non-empty species")
        return None
    return species


zooList = [
    [10, "Alex", "carnivore", "lion"],
    [11, "George", "herbivore", "zebra"],
    [12, "Ferguson", "herbivore", "zebra"],
    [13, "Patrick", "carnivore", "lion"],
    [14, "Morticia", "omnivore", "bear"],
    [15, "David", "omnivore", "bear"]
            ]
start(zooList)

def TestModify():
    pass
    animal_list = [[100, "Animal", "test", "aa"]]