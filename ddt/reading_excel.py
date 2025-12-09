import xlrd

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

def reading_testdata(file_path, sheet_name):
    workbook = xlrd.open_workbook(file_path)
    worksheet = workbook.sheet_by_name(sheet_name)
    rows = worksheet.get_rows()
    header = next(rows)

    d = {}
    for row in rows:
        d[row[0].value] = row[1].value

    return d