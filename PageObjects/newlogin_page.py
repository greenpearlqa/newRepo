class Newlogin:
    def __init__(self,page):
        self.page=page
        self.userid = page.get_by_placeholder("User ID")
        self.useridfill = page.get_by_placeholder("User ID")
        self.password = page.get_by_placeholder("Password")
        self.passwordfill = page.get_by_placeholder("Password")
        self.submit = page.get_by_role("button", name="Login")
    
    def login(self):
        self.userid.click()
        self.useridfill.fill("qateststudent131")
        self.password.click()
        self.passwordfill.fill("123")
        self.submit.click()


