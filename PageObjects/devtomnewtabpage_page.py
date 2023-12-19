from playwright.sync_api import expect
class Newtabpage:

    def studentprogressreport(self, page):
        with page.expect_popup() as page1_info:
            self.studentprogressreport= page.get_by_role("link", name="Student Progress Report")
            self.studentprogressreport.click()
        try:
            self.page2= page1
            locators= self.page2.locator('//*[@id="page-header"]/div/h2')
            expect(locators).to_have_text("Student Progress Reports")

        except NameError:
            print("Student Progress Reports page is not found")
        page1=page1_info.value
        page1.close()