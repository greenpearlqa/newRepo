import time
from playwright.sync_api import expect

from PageObjects.logout_page import logoutpage


class googleloginhomepage:
      
      def __init__(self,page):
      # Initialize the Google link login class with a Playwright page object
            self.page = page
      # Element on page
            self.my_dashboard = page.get_by_role("heading", name="My Dashboard")
            
      def dashboard(self):
      # Click on Dashboard
            self.my_dashboard.click()
            self.page.wait_for_timeout(1000)
      # Validate the text
            expect(self.my_dashboard).to_contain_text("My Dashboard")
            self.page.wait_for_timeout(5000)
      # Logout
            return logoutpage(self.page)