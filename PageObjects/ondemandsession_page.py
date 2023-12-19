import time
from PageObjects.logout_page import logoutpage
from playwright.sync_api import expect
#from Utilities.assertion_validation import assertionandvalidation

class OnDemandSessionPage:

    def __init__(self,page):
    # Initialize the OnDemandSession class with a Playwright page object
      self.page =page
    
    # Elements on the page
      self.subject = page.locator("#ddlLayer1")
      self.course = page.locator("#ddlLayer2")
      self.question = page.locator("#txtQuestion3")

      self.performancesite_question = page.locator("#txtQuestion4")
      self.performance_submit = page.locator('//input[@id="btnSubmit"]')
      self.submit_button = page.get_by_role("button", name="Submit")
      

    def fill_request_on_demand_session_form(self):
    
    # Click on elements and perform actions to fill in Ondemand session details
    # Select "Subject"
      self.subject.click(timeout=0)
      self.subject.select_option("4")
    # Select "Course"
      self.course.select_option("843")   
    # Enter Question details    
      self.question.fill("testing please don't pick") 
    # Click on Submit Button           
      self.submit_button.click(timeout=0)

    def fill_performancesite_on_demand_session_form(self):
    
    # Click on elements and perform actions to fill in Ondemand session details
    # Select "Subject"
      self.subject.click(timeout=0)
      self.subject.select_option("2")
    # Select "Course"
      self.course.select_option("819")   
    # Enter Question details    
      self.performancesite_question.fill("testing please don't pick") 
    # Click on Submit Button           
      self.page.wait_for_timeout(100) 
      self.performance_submit.click(timeout=0)
      self.page.wait_for_timeout(5000) 
      
