import pandas as pd
from datetime import datetime, timedelta

from Utilities.paths import get_bulk_plan_upload_file

class ExcelUpdater:
    def __init__(self):
        self.excel_file_path = get_bulk_plan_upload_file()
        self.sheet_name = 'SchedulePlan'
        self.df = pd.read_excel(self.excel_file_path, sheet_name=self.sheet_name)

    def update_values(self):
        current_date = datetime.now()

        # Set 'END_DATE' and 'START_DATE' to the current date
        self.df.at[0, 'END_DATE'] = current_date.strftime('%d-%b-%y')
        self.df.at[0, 'START_DATE'] = current_date.strftime('%d-%b-%y')

        # Update 'Day 1' based on the 'START_DATE'
        self.df.at[0, 'Day 1'] = current_date.strftime('%A')

        # Update other values based on your requirements
        self.df.at[0, 'USER_NAME'] = 'FevQAStu1020'
        self.df.at[0, 'SCHOOL_ID'] = 18781
        self.df.at[0, 'PROGRAM_ID'] = 'YourProgramID'
        self.df.at[0, 'VERSION_ID'] = 'YourVersionID'
        self.df.at[0, 'TIMEZONE'] = '(GMT-05:00) Eastern Time (US & Canada)'
        self.df.at[0, 'SCHEDULE TYPE'] = 'YourScheduleType'
        self.df.at[0, 'TYPE'] = 'NonRecurring'
        self.df.at[0, 'CAN_STUDENT_EDIT'] = 'No'
        self.df.at[0, 'Day 1'] = 'Monday'
        self.df.at[0, 'Subject 1'] = 3
        self.df.at[0, 'Course ID 1'] = 'YourCourseID'
        self.df.at[0, 'Session Start time 1'] = '18:00'
        self.df.at[0, 'Session Duration 1'] = 30
        

        # Save the updated DataFrame back to the Excel file
        self.df.to_excel(index=False)



