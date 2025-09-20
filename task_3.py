world_champions = {
    2002: "Бразилия",
    2006: "Италия",
    2010: "Испания",
    2014: "Германия",
    2018: "Франция",
}
world_champions[2022] = "Аргентина"
for i in range(len(list(world_champions))):
    print(list(world_champions.keys())[i], "-", list(world_champions.values())[i])

if "Италия" in list(world_champions.values()):
    print("Италия cтановилась чемпионом мира по футболу в 21 веке!")
else:
    print("Италия не выигрывала чемпионат мира по футболу в 21 веке.")
