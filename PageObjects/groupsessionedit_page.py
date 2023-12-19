import openpyxl


class Groupsessionedit:
    def __init__(self, file_path):
        self.file_path = file_path
        self.workbook = openpyxl.load_workbook(file_path)
        self.sheet = self.workbook.active

    def edit_cell(self, cell, new_value):
        self.sheet[cell] = new_value

    def save_changes(self):
        self.workbook.save(self.file_path)