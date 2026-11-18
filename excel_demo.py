from openpyxl import Workbook
wb = Workbook()
ws = wb.active
ws.title = "Sales"
ws.append(["Item", "Amount"])
ws.append(["Pen", 10])
ws.append(["Book", 25])
ws["B4"] = "=SUM(B2:B3)"
wb.save("sales_report.xlsx")
print("Workbook created")

