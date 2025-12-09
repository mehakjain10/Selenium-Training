from openpyxl import Workbook

workbook = Workbook()

worksheet = workbook.active

worksheet.title = 'M16_Data'

worksheet['A1'] = 'name'
worksheet['B1'] = 'place'
worksheet['C1'] = 'phone'
worksheet['D1'] = 'email'

data_list = [
    ['Mehak', 'Delhi', 9832784676, 'mehak@gmail.com'],
    ['Pooja', 'Mysore', 7478338823, 'pooja@gmail.com'],
]

for row in data_list:
    worksheet.append(row)

workbook.save('M16_Data.xlsx')

# workbook.save(r'C:\Users\Mehak Jain\PycharmProjects\SeleniumTraining\screenshots\M16_Data.xlsx')

