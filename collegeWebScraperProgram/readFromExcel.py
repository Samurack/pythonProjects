import openpyxl, pprint

class readingFromExcel:
	def __init__(self, workbook, worksheet):
		self.workbook = workbook
		self.worksheet = worksheet

	def updateExcelSheet(self):
		print('Opening workbook...')
		wb = openpyxl.load_workbook(self.workbook)
		sheet = wb.get_sheet_by_name(self.worksheet)
		print("Reading rows...")
		ExcelColleges = []
		for row in range(1, sheet.max_row + 1):
			ExcelColleges.append(sheet['A' + str(row)].value)

		return ExcelColleges