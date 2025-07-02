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
    new_item = item.copy()
    new_item['taxes'] = new_item['price'] * 0.19
    return new_item

new_items = list(map(add_taxes, items))
print('Old list')
print(items)
print('New list')
print(new_items)