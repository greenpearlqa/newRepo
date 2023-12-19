class sessionwaitingpage:
# Initialize the SelfSchedule class with a Playwright page object
    def __init__(self,page):
        self.page = page
        page.once("dialog", lambda dialog: dialog.dismiss())
        page.get_by_role("button", name="Cancel").click()
        page.goto("https://portal.fevtutor.com/Student/Student")