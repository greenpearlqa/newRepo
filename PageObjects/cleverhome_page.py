class Cleverhomepage:

    def __init__(self, page):
        # Initialize the Cleverhomepage class with a Playwright page object
        self.page = page

        # Elements related to Data Browser
        self.databrowser = page.get_by_role("link", name="user-search Data Browser")
        self.districtadmin = page.get_by_role("tab", name="District Admins")
        self.previousdistrict = page.get_by_test_id("ui-select").get_by_text("keyboard_arrow_down")
        self.newdistrict = page.locator("#react-select-2-input")
        self.newdistrictselect = page.get_by_text("Advantage Charter Academy", exact=True)
        self.DAemail = page.get_by_role("cell", name="100.sjones@nhaschools.com")
        self.daemailselect = page.get_by_role("button", name="Log in as Stephanie Jones")

        # Elements related to Teachers
        self.teachers = page.get_by_role("tab", name="Teachers")
        self.previousteacherdistrict = page.get_by_test_id("ui-select").get_by_text("keyboard_arrow_down")
        self.newteacherdistrict = page.locator("#react-select-2-input")
        self.newteacherdistrictselect = page.get_by_text("Baltimore City Public School District", exact=True)
        self.addfilter = page.get_by_role("button", name="Add Filter")
        self.valuefill = page.locator("#react-select-8-input")
        self.valueselect = page.get_by_text("611e425aa279f2004632d38e", exact=True)
        self.teachername = page.get_by_text("Madyn")
        self.teachernameselect = page.get_by_role("button", name="Log in as Madyn Abeles")

        # Elements related to Students
        self.students = page.get_by_role("tab", name="Students")
        self.addfilter = page.get_by_role("button", name="Add Filter")
        self.property = page.get_by_text("keyboard_arrow_down").nth(1)
        self.id = page.get_by_text("id", exact=True)
        self.value = page.locator("div:nth-child(3) > .DeweySelect--Body > .DeweySelect--Body__control > .DeweySelect--Body__value-container > .DeweySelect--Body__input-container")
        self.idvalue = page.locator("#react-select-5-input")
        self.valueclick = page.get_by_text("61ca3fab1f6490006e065ac4", exact=True)
        self.name = page.get_by_text("Aaliyah")
        self.studentclick = page.get_by_role("button", name="Log in as Aaliyah Gonzalez")

    def databrowser_click(self):
        # Click on Data Browser
        self.databrowser.click()
    
    def districtadmin_click(self):
        # Click on District Admins, select a district, and log in as an admin
        self.districtadmin.click()
        self.previousdistrict.click()
        self.newdistrict.fill("Advantage Charter Academy")
        self.newdistrictselect.click()
        self.DAemail.click()
        self.daemailselect.click()
    
    def teachers_click(self):
        # Click on Teachers, select a district, add filters, and log in as a teacher
        self.teachers.click()
        self.previousteacherdistrict.click()
        self.newteacherdistrict.fill("Baltimore City Public School District")
        self.newteacherdistrictselect.click()
        self.addfilter.click()
        self.property.click()
        self.id.click()
        self.value.click()
        self.valuefill.fill("611e425aa279f2004632d38e")
        self.valueselect.click()
        self.teachername.click()
        self.teachernameselect.click()
    
    def clever_funcpage(self):
        # Navigate to the Clever Functional page for Students, add filters, and log in as a student
        self.students.click()
        self.addfilter.click()
        self.property.click()
        self.id.click()
        self.value.click()
        self.idvalue.fill("61ca3fab1f6490006e065ac4")
        self.valueclick.click()
        self.name.click(timeout=0)
        self.studentclick.click()
