from domain import *

def add_animal(zooList, code, name, type, species):
    new_animal = [code, name, type, species]
    zooList.append(new_animal)


def verify_c(c):
    commands = ["1", "2", "3", "4", "5"]
    if c in commands:
        return True
    return False

def update_animal(zooList, code, new_type):
    for animal in zooList:
        if getCode(animal) == code:
            setType(animal, new_type)


def search_for_code(zooList, code):
    for animal in zooList:
        if getCode(animal) == code:
            return True
    return False

def sort_type(zooList, type):
    new_list = []
    for animal in zooList:
        if getType(animal) == type:
            new_list.append(animal)
    bubble_sort(new_list)
    return new_list

def bubble_sort(lst):
    for i in range(0, len(lst)):
        for j in range(i+1, len(lst)):
            if getName(lst[i])[0] > getName(lst[j])[0]:
                lst[i] , lst[j] = lst[j], lst[i]

def change_type_by_species(zooList, type, species):
    for animal in zooList:
        if getSpecies(animal) == species:
            setType(animal, type )