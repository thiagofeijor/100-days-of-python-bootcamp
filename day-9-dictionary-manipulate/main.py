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
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = visits
  new_country["cities"] = cities
  travel_log.append(new_country)

include_new = True

while include_new:
  country = input("Type the country name:\n")
  visits = input("Type numbers of visits:\n")

  cities = []
  cities_include_new = True

  while cities_include_new:
    city = input("Type the city name:\n")
    cities.append(city)

    answer = input("Include other city?(yes|no)\n")
    cities_include_new = answer == 'yes'

  add_new_country(country, visits, cities)
  answer = input("Include other?(yes|no)\n")
  include_new = answer == 'yes'

print(travel_log)

