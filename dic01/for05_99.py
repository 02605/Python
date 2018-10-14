cities = {
        "XiAn": {
            "nation": "china",
            "population": 600,
            "describe": "my hometown",
            },
        "LangFang": {
            "nation": "china",
            "population": 200,
            "describe": "my study city",
            },
        "Roman": {
            "nation": "Italian",
            "population": 100,
            "describe": "beautiful city",
            }
        }
for city, infos in cities.items():
    print("\nCity:",city)
    print("\tNation:",infos["nation"])
    print("\tPopulation:"+str(infos['population']))
    print("\tDescribe:"+infos['describe'])
        #print(infod)
