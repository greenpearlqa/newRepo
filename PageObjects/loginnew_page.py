from PageObjects.home_page import homepage

class LoginnewPage:

    def __init__(self,page):
       self.page = page
       self.user_name = page.get_by_placeholder("User ID")
       self.Password = page.get_by_placeholder("Password")
       self.user_email = page.get_by_placeholder("Email")
       self.login_button= page.get_by_role("button", name="Login")
       self.submit_button = page.get_by_role("button", name="Submit")
       self.tutor_email = page.get_by_placeholder("User ID")
       self.tutor_pwd = page.get_by_placeholder("Password")

    def username(self, username):
        self.user_name.click(timeout=0)
        self.user_name.fill(username)
    
    def useremail(self, useremail):
        self.user_email.click(timeout=0)
        self.user_email.fill(useremail)

    def tutoremail(self, tutoremail):
        self.tutor_email.click(timeout=0)
        self.tutor_email.fill(tutoremail)

    def password(self, password):
        self.Password.click(timeout=0)
        self.Password.fill(password)

    def tutorpwd(self, tutorpwd):
        self.tutor_pwd.click(timeout=0)
        self.tutor_pwd.fill(tutorpwd)

    def loginbutton(self):
        self.login_button.click(timeout=0)

    def submitbutton(self):
        self.submit_button.click(timeout=0)
        
    def User_login(self):
        self.user_name.fill("qa10586teststudent279")
        self.Password.fill("123")
        self.loginbutton()
        return homepage(self.page)