from playwright.sync_api import expect
from PageObjects.myprogressreport_page import Myprogressreport
from PageObjects.ondemandsession_page import OnDemandSessionPage
from PageObjects.selfschedule_page import SelfschedulePage

class homepage:
   # Initialize the homepage class with a Playwright page object
    def __init__(self,page):
      self.page =page 
       # Elements on the page
      self.my_dashboard = page.get_by_role("heading", name="My Dashboard")
      self.On_demand_session = page.get_by_role("link", name="Z On Demand Session")
      self.Self_schedule = page.get_by_role("link", name="My Schedule") 
      self.my_progress_report = page.get_by_role("link", name=" My Progress Report")     

    def dashboard(self):
       # Click on Dashboard of homepage and return ondemandsessionpage
       self.my_dashboard.click()
       expect(self.my_dashboard).to_contain_text("My Dashboard")
       return OnDemandSessionPage(self.page)
    
    def click_on_demand_session(self):
       # Click on Request an Ondemand session Button after that it will redirect to Ondemandsession creation page
       self.On_demand_session.click(timeout=0)
       return OnDemandSessionPage(self.page)
    
    def click_selfschedule(self):
       # Click on My Schedule button after that it will redirect to the Self scheduel creation page
       self.Self_schedule.click()
       return SelfschedulePage(self.page)
    
    def click_my_progress_report(self):
       self.my_progress_report.click()
       return Myprogressreport(self.page)

   