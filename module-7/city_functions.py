# Michael Benko
# 2026-09-19
# CSD325-302E Advanced Python (2267-DD)
# Module 7.2 Assignment

def get_city_country(city, country, language=None, population=None):
    if population and language:
        full_name = f"{city}, {country} - population {population}, {language}"
    elif population:
        full_name = f"{city}, {country} - population {population}"
    elif language:
        full_name = f"{city}, {country}, {language}"
    else:
        full_name = f"{city}, {country}"
    return full_name

print(get_city_country("Santiago", "Chile"))
print(get_city_country("Tokyo", "Japan", population=14200000))
print(get_city_country("Manila", "Philippines", population=14000000, language="Tagalog"))