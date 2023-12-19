from datetime import date, timedelta
import datetime
import time
from playwright.sync_api import expect
from Utilities.assertion_validation import assertionandvalidation

class SelfschedulePage:

    def __init__(self, page):
    # Initialize the SelfSchedule class with a Playwright page object
      self.page = page
    # Elements on the page
      self.program = page.locator("#ddlprogram")
      self.subject = page.locator("#ddlsubject")
      self.type = page.get_by_label("Weekly")
      self.test = page.get_by_placeholder("I need help with.")
      self.testenter = page.get_by_placeholder("I need help with.")
      self.onetimecheck = page.get_by_label("One-Time")
      self.enddateselect = page.get_by_text("Date: End date:")
      self.onetimeplantime = page.locator("a")
 
    def click_self_schedule_weekly(self):
    # Create an assertionandvalidation instance
      selfschedule_page = assertionandvalidation()
      selfschedule_page.click_myschedulevalidation(self.page)
    # Select "Program"
      self.program.select_option("string:0")
      self.page.wait_for_timeout(2000)
    # Select "Subject"
      self.subject.select_option("string:1")
    # Select "Type"
      self.type.check()
    # Add "Comment"
      self.test.click()
      self.testenter.fill("Testing don't pick")
                
    def click_self_schedule_onetime(self):
    # Select "Program"
      self.program.select_option("string:0")
    # Select "Subject"
      self.subject.select_option("string:1")
    # Select "Type"
      self.onetimecheck.click()
    # Add "Comment"
      self.test.click()
      self.testenter.fill("Testing don't pick")
    # Select "Today's Date and Time"
      self.enddateselect.click()
      self.onetimeplantime.first.dblclick()
