from Utilities.assertion_validation import assertionandvalidation

class Adminsessionpage:

    def __init__(self, page):
        # Initialize the Adminsessionpage class with a Playwright page object
        self.page = page

        # Elements on the page
        self.student_list = page.get_by_role("link", name="View Student List")
        self.search = page.get_by_role("link", name="Advanced Search")
        self.user_name = page.get_by_placeholder("User Name")
        self.user_search = page.get_by_role("button", name="Search")
        self.schedule = page.get_by_role("button", name="Scheduled")
        self.select_student_checkbox = page.locator('input[name="chkStudents"]')
        self.calendar_view = page.get_by_role("button", name="View Calendar")

    def fill_request_on_admin_session_schedule_details(self):
        # Create an assertionandvalidation instance
        adminschedule_page = assertionandvalidation()

        # Click on "View Student List"
        self.student_list.click(timeout=0)

        # Click on "Advanced Search"
        adminschedule_page.click_viewstudentvalidation(self.page)
        self.search.click(timeout=0)

        # Enter user name and search
        self.user_name.click(timeout=0)
        self.user_name.fill("Fevqastu1025")

        #Regression test with program
        #self.user_name.fill("Fevqastu1019")
        #self.user_name.fill("Fevqastu1020")

        self.user_search.click(timeout=0)

        # Click on "Scheduled"
        self.schedule.click(timeout=0)
        self.page.wait_for_timeout(2000)

        # Check the first student's checkbox
        self.select_student_checkbox.first.check(timeout=0)

        # Click on "View Calendar"
        self.calendar_view.click(timeout=0)

    def delete_session(self):
        
        # Click on "View Calendar"
        self.calendar_view.click(timeout=0)

    def fill_schedule_session_details(self):
        # Create an assertionandvalidation instance
        adminschedule_page = assertionandvalidation()
        # Click on "View Student List"
        self.student_list.click(timeout=0)
        # Click on "Advanced Search"
        adminschedule_page.click_viewstudentvalidation(self.page)
        self.search.click(timeout=0)
        # Enter user name and search
        self.user_name.click(timeout=0)
        self.user_name.fill("Fevqastu1025")
        
        #Regression test with program
        #self.user_name.fill("Fevqastu1019")
        
        self.user_search.click(timeout=0)
        # Click on "Scheduled"
        self.schedule.click(timeout=0)
        self.page.wait_for_timeout(2000)
        # Check the first student's checkbox
        self.select_student_checkbox.first.check(timeout=0)
        # Click on "View Calendar"
        self.calendar_view.click(timeout=0)
