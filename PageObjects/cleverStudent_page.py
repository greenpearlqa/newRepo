class Studentpagelocators:

    def __init__(self, page):
        # Initialize the Studentpagelocators class with a Playwright page object
        self.page = page

        # Open a new student page and capture elements within the page
        with page.expect_popup() as newstudentpage_info:
            self.studentclick = page.get_by_role("button", name="Log in as Aaliyah Michelle Gonzalez")
        
        studentpage = newstudentpage_info.value
        
        # Elements related to the student page
        self.ondemandclick = studentpage.get_by_role("link", name="Z On Demand Session")
        self.ondemandcancel = studentpage.locator("#modalMsg").get_by_text("Cancel")
        self.myschedule = studentpage.get_by_role("link", name=" My Schedule")
        self.sessionhistory = studentpage.get_by_role("link", name=" Session History")
        self.myjourney = studentpage.get_by_role("link", name=" My Journey")
        self.myprogressreport = studentpage.get_by_role("link", name=" My Progress Report")
        self.preposttest = studentpage.get_by_role("link", name=" Pre & Post Test Assignments")
        self.myaccount = studentpage.get_by_role("link", name=" My Account & Profile")
        self.mylearning = studentpage.get_by_role("link", name=" My Learning Plan")
        self.stupage = studentpage  # A reference to the entire student page
        self.cleverclose = page.get_by_role("button", name="close modal window")

    def clever_studentpage(self):
        # Click on various elements on the student page
        self.ondemandclick.click()
        self.ondemandcancel.click()
        self.myschedule.click()
        self.sessionhistory.click()
        self.myjourney.click()
        self.myprogressreport.click()
        self.preposttest.click()
        self.myaccount.click()
        self.mylearning.click()
        
        # Close the student page and the Clever modal
        self.stupage.close()
        self.cleverclose.click()
