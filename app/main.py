import utils

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

def run():
    keys, values = utils.get_population()
    print(keys, values)

    country = input('Enter country name: ')

    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__':
    run()