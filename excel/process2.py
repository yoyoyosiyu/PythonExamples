
# 输入文件
file_input = "d:/data1.csv"

# 输出文件
file_output = "d:/data2.csv"

file1 = open(file_input, "r")

areas = {}

while True:
    line = file1.readline()
    if len(line) == 0:
        break
    line = line.replace("\n", '')
    parts = line.split(",")

    area = parts[3]
    product = parts[7]
    quantity = int(parts[8])
    price = parts[9]

    if area not in areas:
        areas[area] = {}

    content = areas[area]
    if product not in content:
        content[product] = 0
    content[product] = content[product] + quantity

file1.close()

file = open(file_output, "w+")

print(areas)

for area in areas:
    products = areas[area]
    for productName in products:
        productCount = products[productName]
        file.write(area+",")
        file.write(productName+",")
        file.write(str(productCount)+"\n")

file.close()

