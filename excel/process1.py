import xlwings as xw
import re

'''
将系统给的excel表格输出为中间格式，每行包括一个订单行（不是一个订单），包含了以下的列
订单编号，省份，城市，行政区，详细地址，联系电话，联系人，套餐名称，套餐数量，套餐单价
'''

# 输入文件
file_input = "d:/test.xlsx"

# 输出文件
file_output = "d:/data1.csv"

# 输入文件中数据的开始行号
startLine = 4


def process_address(address):
    result = []
    parts = str.split(address, "\n")
    for i in range(len(parts) - 1, -1, -1):
        if len(parts[i]) == 0:
            continue
        result.append(parts[i])
    return result


def process_details(details, regex):
    result = []

    parts = str.split(details, "\n")
    for part in parts:
        if part is None or len(part) == 0:
            continue

        result.append(analysis_data(part, regex))

    return result


def analysis_data(data, regex):

    result = regex.match(data)
    if result is None:
        return result
    return result.groups()


def process_sheet(sheet, startLine, regex):
    file = open(file_output, "w+")

    location_regex = re.compile("^(\\S*) *(\\S*) *(\\S*) *(\\S*)", re.I)

    rowCount = 0
    while True:
        Ax = sheet.range('A' + str(startLine)).value
        if Ax is None or len(Ax) == 0:
            break

        print(Ax)

        address = process_address(sheet.range('J' + str(startLine)).value)
        details = process_details(sheet.range('K' + str(startLine)).value, regex)

        for detail in details:
            file.write(Ax + ",")
            for part in address:
                location_parts = location_regex.match(part).groups()
                for location_part in location_parts:
                    if len(location_part) == 0:
                        continue
                    file.write(location_part+",")

            file.write(detail[0]+","+detail[1]+","+detail[2]+",")
            file.write("\n")

        startLine += 1
        rowCount += 1

    file.close()

    print(str(rowCount) + ' Rows')


app = xw.App(visible=None, add_book=False)
book = app.books.open(file_input)
sheet = book.sheets[0]


rx = re.compile("^(\\S*) *\[(\\d+) \* ((\\d+).?(\\d*))\]")

process_sheet(sheet, startLine, rx)

book.close()
