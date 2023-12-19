# Import the assertion and validation functions from the assertion_validation module
from Utilities.assertion_validation import assertionandvalidation
import time
# Define the StudentPretest class
class StudentPretest:

    # Constructor for StudentPretest, takes a 'page' parameter
    def __init__(self, page):
        self.page = page
        self.assert_validate = assertionandvalidation()

        # Define locators for page elements
        self.page_header = page.locator('#page-header').locator('h2')
        self.user_id = page.get_by_placeholder("User ID")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.prepost_assignment_link = page.get_by_role("link", name="Pre & Post Test Assignments")
        self.assessment_link = page.locator(".table tbody tr:nth-child(1) td:nth-child(1) .asstest")
        self.next_button =  page.locator("[id=\"lrn_assess_next_btn\"]")
        self.finish_button = page.get_by_role("button", name="Finish")
        self.yes_button = page.get_by_role("button", name="Yes")
        self.close_button = page.get_by_role("button", name="Close")
        self.result_link =  page.get_by_role("link", name="Results")
        self.popup_assessement_button = page.locator('#btnViewAssiTest')
        self.assessment_result_link = page.locator(".table tbody tr:nth-child(1) td:nth-child(1) .restest")

    # Method for performance student login
    def performance_student_login(self):
        self.user_id.fill("qa-test-student-10")
        self.password.fill("123")
        self.login_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "My Dashboard", None)
        
    def view_assignment_popup_click(self):
        time.sleep(10)
        assessement_modal_style_attribute = self.page.locator("#NewAssiTest").get_attribute('style')
        if assessement_modal_style_attribute is not None:
            self.popup_assessement_button.click(timeout=0)
            self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Pre & Post Testing", None)
            self.assert_validate.validate_student_assessement_page('check_visibility', self.assessment_link, "student assessement link", None)
        else:
            self.prepost_assignment()

    # Method to navigate to the pre & post test assignments
    def prepost_assignment(self):
        self.prepost_assignment_link.click(timeout=0)
        self.assert_validate.validate_studentassessment_page_header(self.page_header, "Pre & Post Testing")
        self.assert_validate.validate_studentassessment_visibility(self.assessment_link, "student assessment link")
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Pre & Post Testing", None)
        self.assert_validate.validate_student_assessement_page('check_visibility', self.assessment_link, "student assessement link", None)

    def assessement_test_click(self):
        self.assessment_link.click(timeout=0)
        self.assert_validate.validate_studentassessment_visibility(self.page.get_by_role("link", name="Item 1 , Unattempted."), "Student assessment first question")
            
    # Method to take the assessment
        self.assert_validate.validate_student_assessement_page('check_visibility', self.page.get_by_role("link", name="Item 1 , Unattempted."), "Question 1", None)        

    def take_assessment(self):
        self.page.get_by_label("How are Mr. Deane and his daughter different from each other?").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("How are Mr. Deane and his daughter different from each other?"), "Question 1", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 2 , Unattempted."), "Question 2", "pagination-active")

        self.page.get_by_label("the age difference between the brother and sister").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("the age difference between the brother and sister"), "Question 2", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 3 , Unattempted."), "Question 3", "pagination-active")

        self.page.get_by_label("her influence on Adrian").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("her influence on Adrian"), "Question 3", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 4 , Unattempted."), "Question 4", "pagination-active")

        self.page.get_by_label("resign or surrender").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("resign or surrender"), "Question 4", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 5 , Unattempted."), "Question 5", "pagination-active")

        self.page.get_by_label("Paragraph 6").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("Paragraph 6"), "Question 5", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 6 , Unattempted."), "Question 6", "pagination-active")
        
        self.page.get_by_label("physical descriptions of the other characters").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("physical descriptions of the other characters"), "Question 6", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 7 , Unattempted."), "Question 7", "pagination-active")
       
        self.page.get_by_label("her prideful disposition").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("her prideful disposition"), "Question 7", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 8 , Unattempted."), "Question 8", "pagination-active")

        self.page.get_by_label("People often lose their sense of wonder with age.").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("People often lose their sense of wonder with age."), "Question 8", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 9 , Unattempted."), "Question 9", "pagination-active")

        self.page.get_by_label("He offered his autobiography free of charge.").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("He offered his autobiography free of charge."), "Question 9", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 10 , Unattempted."), "Question 10", "pagination-active")

        self.page.get_by_label("Think positive.").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("Think positive."), "Question 10", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 11 , Unattempted."), "Question 11", "pagination-active")

        self.page.get_by_label("develop a creative marketing strategy").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("develop a creative marketing strategy"), "Question 11", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 12 , Unattempted."), "Question 12", "pagination-active")

        self.page.get_by_label("objectively").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("objectively"), "Question 12", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 13 , Unattempted."), "Question 13", "pagination-active")

        self.page.get_by_label("to develop the idea that Mr. Genin was not able to access every possible market for his product").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("to develop the idea that Mr. Genin was not able to access every possible market for his product"), "Question 13", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 14 , Unattempted."), "Question 14", "pagination-active")

        self.page.get_by_label("to request information from the audience").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("to request information from the audience"), "Question 14", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 15 , Unattempted."), "Question 15", "pagination-active")

        self.page.get_by_label("the high rate of literacy in the country").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("the high rate of literacy in the country"), "Question 15", None)
        self.next_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_class', self.page.get_by_role("link", name="Item 16 , Unattempted."), "Question 16", "pagination-active")

        self.page.get_by_label("The shoes can improve your game.").check(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_ischecked', self.page.get_by_label("The shoes can improve your game."), "Question 16", None)

        self.finish_button.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_visibility', self.yes_button, "Close button", None)

        self.yes_button.click(timeout=0)

    # Method to view test results
    def test_result(self):
        self.prepost_assignment_link.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_text', self.page_header, "Pre & Post Testing", None)
        self.assert_validate.validate_student_assessement_page('check_visibility', self.result_link, "Result page", None)

        self.result_link.click(timeout=0)
        self.assert_validate.validate_student_assessement_page('check_visibility', self.page.locator("#res").locator('table'), "Results table", None)
