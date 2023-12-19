# Import the assertion and validation functions from the assertion_validation module
from Utilities.assertion_validation import assertionandvalidation

# Define the StudentAssessment class
class StudentAssessment:

    # Constructor for StudentAssessment, takes a 'page' parameter
    def __init__(self, page):
        self.page = page
        self.assert_validate = assertionandvalidation()

        # Define locators for page elements
        self.page_header = page.locator('#page-header').locator('h2')
        self.user_id = page.get_by_placeholder("User ID")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.assessment_link = page.get_by_role("link", name="Assessment")
        self.assign_testlink = page.get_by_role("link", name="Assign Test")
        self.user_name = page.get_by_placeholder("User Name")
        self.search_button = page.get_by_role("button", name="Search")
        self.studentdetails_row_checkbox =  page.locator("#grdProgresReportList table tbody tr:nth-child(1) td:nth-child(1) input")
        self.assigntest_button = page.get_by_role("button", name="Assign Test")
        self.studentsubject_dropdown = page.locator("#drpStuSubject")
        self.testtype_dropdown = page.locator("#ddlTestType")
        self.text_title = page.locator("#txtTit")
        self.text_description = page.locator("#txtDes")
        self.testid_span =  page.get_by_role("cell", name="+ English II PreTest").locator("span")
        self.testid_radio = page.get_by_role("radio")
        self.assign_button = page.get_by_role("button", name="Assign")
    
    # Method for performance admin login
    def performance_admin_login(self):
        self.user_id.fill("devtom")
        self.password.fill("fev2022")
        self.click_loginbutton()
        self.click_dashboardLink()
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Dashboard", None)

    # Method for assessment login
    def assessment_login(self):
        self.click_assessmentlink()
        self.assign_testlink.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Assign Test", None)
    
    # Method to assign a test to a user
    def assign_test_user(self):
        self.user_name.fill("qa-test-student-10")
        self.click_searchbutton()
        self.assert_validate.validate_student_assessement_page('check_visibility', self.studentdetails_row_checkbox, "student row checkbox", None)
        self.studentdetails_row_checkbox.check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.studentdetails_row_checkbox, "Student details row", None)
        self.click_assigntestbutton()
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Pre Test Details", None)

    # Method to fill in test details
    def fill_test_details(self):
        self.studentsubject_dropdown.select_option(label="English")
        self.testtype_dropdown.select_option(label="Pre Test")
    
    # Method to search for a test
    def search_test(self):
        self.text_title.fill("English II PreTest")
        self.text_description.fill("english test")
        self.click_searchbutton()
        self.assert_validate.validate_student_assessement_page('check_visibility', self.testid_span, "Searched test result", None)

    # Method to assign a test
    def assign_test(self):
        self.testid_span.click()
        self.assert_validate.validate_student_assessement_page('check_visibility', self.testid_radio, "Searched test activity radio", None)
        self.testid_radio.click()
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.testid_radio, "Searched test activity radio", None)
        self.click_assignbutton()
        print(f"Assign button clicked and test assigned successfully")

    # Helper method to click the login button
    def click_loginbutton(self):
        self.login_button.click(timeout=0)

    # Helper method to click the dashboard link
    def click_dashboardLink(self):
        self.dashboard_link.click(timeout=0)

    # Helper method to click the assessment link
    def click_assessmentlink(self):
        self.assessment_link.click(timeout=0)

    # Helper method to click the search button
    def click_searchbutton(self):
        self.search_button.click(timeout=0)

    # Helper method to click the assign test button
    def click_assigntestbutton(self):
        self.assigntest_button.click(timeout=0)

    # Helper method to click the assign button
    def click_assignbutton(self):
        self.assign_button.click(timeout=0)
        print(f"Assign button clicked and test assigned successfully")
