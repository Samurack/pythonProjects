import openpyxl, pprint
from Createcollege import CollegeClass

class writeToExcel:
	def __init__(self, workbook, worksheet, listOfColleges):
		self.workbook = workbook
		self.worksheet = worksheet
		self.listOfColleges = listOfColleges

	def updateExcelSheet(self):
		print('Opening workbook...')
		wb = openpyxl.load_workbook(self.workbook)
		sheet = wb.get_sheet_by_name(self.worksheet)
		print("Reading rows...")
		ExcelColleges = []
		for row in range(1, sheet.max_row + 1):
			ExcelColleges.append(sheet['A' + str(row)].value)

		print(ExcelColleges)
		for aList in self.listOfColleges:
		   if aList.getCollegeName() in ExcelColleges:
		   	row = ExcelColleges.index(aList.getCollegeName()) + 1
		   	sheet['B' + str(row)].value = aList.getCollegeCost()
		wb.save(self.workbook)