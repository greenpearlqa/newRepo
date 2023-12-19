class BulkOnDemandSchedule:

    def __init__(self, page):
        # Initialize the Publishsession class with a Playwright page object
        self.page = page
        self.session_button = page.get_by_role("link", name="  Session")
        self.bulkondemandsession_button = page.get_by_role("link", name="Bulk On-Demand Session Creation", exact=True)
       
    def sessionbutton(self):
            self.session_button.click(timeout=0)
            self.page.wait_for_timeout(1000)

    def bulkondemandsessionschedulebutton(self):
            self.bulkondemandsession_button.click(timeout=0)
            self.page.wait_for_timeout(2000)