import utils

def run():
    keys, values = utils.get_population()
    print(keys, values)

    data = [
        {
            'Country': 'China',
            'Population': 100000
        },
        {
            'Country': 'Bolivia',
            'Population': 600000
        }
    ]

    country = input('Enter country name: ')

    result = utils.population_by_country(data, country)
    print(result)