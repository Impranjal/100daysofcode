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
country = input("enter the name of country you have visited ")
no_of_times = int(input(f"Times visited {country}"))
cities_visited = eval(input(f"The cities visited in {country} "))

def add_new_country(country,no_of_times,cities_visited):
    dict2 = dict()
    dict2['country'] = country
    dict2['visits'] = no_of_times
    dict2['cities'] = cities_visited
    travel_log.append(dict2)
    print(travel_log)
    return travel_log
add_new_country(country,no_of_times, cities_visited)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
        

        
        