from playwright.sync_api import expect
from Utilities.assertion_validation import assertionandvalidation
class StudentIlp:

#Login student and navigating to my learning plan page
    def __init__(self, page):
        self.page= page
        self.assert_validate = assertionandvalidation()
        self.userid= page.get_by_placeholder("User ID")
        self.userfill= page.get_by_placeholder("User ID")
        self.password= page.get_by_placeholder("Password")
        self.passwordfill= page.get_by_placeholder("Password")
        self.login= page.get_by_role("button", name="Login")
        self.ilppage= page.locator('//*[@id="ulLeftMenu"]').get_by_role("link", name="My Learning Plan")
        self.lessondrop= page.locator("#ddlLearningPlan")
        self.tab= page.get_by_role("link", name="Future")

#Action for student login, navigating to my learning plan page & select the ilp lesson

    def student_login(self, page):
        self.userid.click(timeout=0)
        self.userfill.fill("qateststudent131")
        self.password.click(timeout=0)
        self.passwordfill.fill("123")
        self.login.click(timeout=0)
        page.wait_for_timeout(5000)

    def mylearning_page(self,page):
        self.ilppage.click(timeout=0)
        self.assert_validate.validate_mylearning_page_header(self.page)
        self.lessondrop.select_option(index=2)
        page.wait_for_timeout(5000)
        self.tab.click(timeout=0)
        self.assert_validate.validate_mylearning_tab_selection(self.tab)
        page.wait_for_timeout(5000)
        self.assert_validate.studentilp_validation(self.page)
        

