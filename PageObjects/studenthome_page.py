from playwright.sync_api import expect

from PageObjects import studenthistorydownload_page

#from PageObjects.studenthistorydownload_page import studenthistorydownloadpage

class studenthomepage:
      # Initialize the SelfSchedule class with a Playwright page object
       def __init__(self,page):
             self.page = page
             self.my_dashboard = page.get_by_role("heading", name="My Dashboard")
            
       def dashboard(self):
             self.my_dashboard.click()
             expect(self.my_dashboard).to_contain_text("My Dashboard")
             return studenthistorydownload_page(self.page)
       