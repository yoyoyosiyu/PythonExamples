from openpyxl import load_workbook

wb = load_workbook('20200414.xlsx')

config = {
    'sheet': '汇总',
    'category': 'a',
    'name': 'c',
    'price': 'e',
    'first_row': 2
}

sheet = wb[config['sheet']]
i = 1 if 'first_row' not in config.keys() else config['first_row']
while sheet['a' + str(i)].value is not None:
    category = sheet[config['category'] + str(i)].value
    name = sheet[config['name'] + str(i)].value
    price = sheet[config['price'] + str(i)].value
    print("category: %s, name: %s, price: %s" % (category, name, price))
    i = i + 1
