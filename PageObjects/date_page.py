import datetime

class Datepage:

    def __init__(self,page):
        self.page = page
        self.todaydate = page.locator('xpath = //button[@class="fev_monthview_cellbtn ng-scope fev_monthview_selected"]')
        self.enddatecalendar = page.get_by_role("button", name="").nth(1)
        self.enddate = page.locator('xpath=//button[@class="btn btn-sm btn-info uib-datepicker-current ng-binding"]')
    
    def select_date(self):
        self.todaydate.click(timeout=0)

    def select_enddate(self):
        self.enddatecalendar.click()
        self.enddate.click()

    def select_day(self):
        weekday_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        current_day = datetime.datetime.today().strftime('%A')
    
        if current_day in weekday_names:
            self.page.get_by_label(current_day).check()



