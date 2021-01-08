travel_log = [
{
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
},
{
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country, visits, cities):
    # more verbose but easier to understand maybe
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

    # easier in a single line
    #travel_log.append({"country":country, "visits": visits, "cities": cities})


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)