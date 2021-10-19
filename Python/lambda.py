people = [
    {"name": "Harry", "House": "Gryffindor"},
    {"name": "Cho", "House": "Ravenclae"},
    {"name": "Draco", "House": "Slytherin"},
]

# tradisional ways
# def f(person):
#     return person["name"]
# people.sort(key=f)
# print(people)

# lambda ways
people.sort(key=lambda person: person["name"])
print(people)
