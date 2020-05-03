# 输入文件
file_input = "d:/data2.csv"

# 输出文件
file_output = "d:/data3.csv"

file = open(file_input, "r")

count = {}

while True:
    line = file.readline()
    if len(line) == 0:
        break
    line = line.replace("\n", '')
    parts = line.split(",")

    print(parts)

    area = parts[0]
    product = parts[1]
    quantity = int(parts[2])

    if product not in count:
        count[product] = 0
    count[product] += quantity

print(count)

file = open(file_output, "w+")

for productName in count:
    file.write(productName+"," + str(count[productName])+"\n")

file.close()