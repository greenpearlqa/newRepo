import time

# Define the Joinnow class
class Joinnow:
    def __init__(self, page):
        self.page = page

        # Define locators for elements on the page
        self.joinnow = page.locator("#divJoinNow div")
        self.sessionrating = page.locator("span").filter(has_text="3").nth(1)
        self.tutorrating = page.locator("span").filter(has_text="4").nth(3)
        self.studentcomments = page.get_by_placeholder("Comments.")
        self.studentcommentsfill = page.get_by_placeholder("Comments.")
        self.submit = page.get_by_role("button", name="SUBMIT")

        self.french_sessionrating = page.locator("span").filter(has_text="2").nth(1)
        self.french_tutorrating = page.locator("span").filter(has_text="3").nth(3)
        self.french_comment = page.get_by_placeholder("Commentaires.")
        self.submit_feedback = page.get_by_role("button", name="SOUMETTRE")

        self.spanish_sessionrating = page.locator("span").filter(has_text="2").nth(1)
        self.spanish_tutorrating = page.locator("span").filter(has_text="3").nth(3)
        self.spanish_comment = page.get_by_placeholder("Comentarios.")
        self.spanish_feedback = page.get_by_role("button", name="ENTREGAR")

    # Click the "Join Now" button
    def click_joinnow(self):
        self.joinnow.first.dblclick()

    # Provide student feedback
    def student_feedback(self):
        self.sessionrating.click()
        self.tutorrating.click()
        self.studentcomments.click()
        self.studentcommentsfill.fill("Testing")
        time.sleep(5)
        self.submit.click()

    # Provide French student feedback
    def french_student_feedback(self):
        self.french_sessionrating.click()
        self.french_tutorrating.click()
        self.french_comment.click()
        self.french_comment.fill("Testing")
        time.sleep(5)
        self.submit_feedback.click()

    # Provide Spanish student feedback
    def spanish_student_feedback(self):
        self.spanish_sessionrating.click()
        self.spanish_tutorrating.click()
        self.spanish_comment.click()
        self.spanish_comment.fill("Testing")
        time.sleep(5)
        self.spanish_feedback.click()
