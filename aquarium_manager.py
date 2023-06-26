import json

f = open("aquarium.json", encoding="utf8")
data_aquarium = json.load(f)
animals = data_aquarium["data"]


def verif_fish(animal):
    if animal["type"] == "fish":
        return True
    return False


animal_fish = list(filter(verif_fish, animals))


def animal_name(animal):
    return animal["name"]


animal_fish_name = list(map(animal_name, animal_fish))
print(animal_fish_name)


def assign_to_tank(animals, names_select, new_tank_number):
    def change_tank_number(animal):
        if animal["name"] in names_select:
            animal["tank number"] = 42
        return animal

    return list(map(change_tank_number, animals))


new_aquarium = assign_to_tank(animals, animal_fish_name, 42)
print(new_aquarium)
