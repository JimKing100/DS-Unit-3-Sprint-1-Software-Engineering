from random import randint, sample, uniform, choice
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(0, num_products):
        adj = choice(ADJECTIVES)
        noun = choice(NOUNS)
        new_name = adj + ' ' + noun
        new_price = randint(5, 100)
        new_weight = randint(5, 100)
        new_flame = uniform(0, 2.5)
        new_product = Product(name=new_name,
                              price=new_price,
                              weight=new_weight,
                              flammability=new_flame)
        products.append(new_product)
    return products


def inventory_report(products):

    unique_list = []
    unique_count = 0
    for i in range(0, len(products)):
        if products[i].name not in unique_list:
            unique_list.append(products[i].name)
            unique_count = unique_count + 1

    sum_price = 0
    for i in range(0, len(products)):
        sum_price = sum_price + products[i].price
    avg_price = sum_price / len(products)

    sum_weight = 0
    for i in range(0, len(products)):
        sum_weight = sum_weight + products[i].weight
    avg_weight = sum_weight / len(products)

    sum_flame = 0
    for i in range(0, len(products)):
        sum_flame = sum_flame + products[i].flammability
    avg_flame = sum_flame / len(products)

    print('ACME INVENTORY REPORT')
    print('Unique product names:', unique_count)
    print('Average price:', avg_price)
    print('Average weight:', avg_weight)
    print('Average flammmability:', avg_flame)
    pass


if __name__ == '__main__':
    inventory_report(generate_products())
