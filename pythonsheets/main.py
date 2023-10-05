import gspread

gc = gspread.service_account(filename='credentials.json')
sh = gc.open_by_key('1hVTzDmsiACZmgVjMkGsWytmyh9VC3M5awQ8_yF61_lE')
worksheet = sh.sheet1

#res = worksheet.get_all_records()
#res = worksheet.get_all_values()
#res = worksheet.row_values(1)
#res = worksheet.col_values(1)
#res = worksheet.get('A2')

#user = ["Susan", 25, "Sydney"] #CREATE
#worksheet.insert_row(user, 3)

#worksheet.update_cell(6,2, 28)  #UPDATE

#worksheet.delete_rows(1)  #DELETE