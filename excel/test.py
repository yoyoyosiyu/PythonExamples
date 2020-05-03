import xlwings as xw
print("hello,world!")

book = xw.Book()
sheet = book.sheets['Sheet1']
sheet.range('A1').value = 'Foo 1'
book.save('test.xlsx')
