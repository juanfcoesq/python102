items = [
    {
        'product' : 'camisa',
        'price' : 100
    },
    {
        'product' : 'pantalón',
        'price' : 200
    },
    {
        'product' : 'chuleta',
        'price' : 300
    }
]

prices = list(map(lambda item: item['price'], items))
print(items)
print(prices)

def add_taxes(item):
    item['taxes'] = item['price'] * 0.19
    return item

new_items = list(map(add_taxes, items))
print(items)
print(new_items)