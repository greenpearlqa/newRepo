import time
from PageObjects.googlelinkhome_page import googleloginhomepage

class googleloginpage:

     def __init__(self,page):
     # Initialize the googleloginpage class with a Playwright page object
          self.page = page
          #self.portal_site= page.goto("https://portal.fevtutor.com/")
     # Elements on the page
          self.user_name= page.get_by_placeholder("User ID")
          self.googlelogin_button= page.get_by_role("link", name="Google")
          self.user_email= page.get_by_role("textbox", name="Email or phone")
          self.next_button = page.get_by_role("button", name="Next")
          self.user_emailpassword = page.get_by_role("textbox", name="Enter your password")
          self.nextpassword_button = page.get_by_role("button", name="Next")

     # Method to enter the username
     def username(self, username):
        self.user_name.click(timeout=0)
        self.user_name.fill(username)

     # Method to click the Google login button
     def googleloginbutton(self):
          self.googlelogin_button.click(timeout=0)
          self.page.wait_for_timeout(5000)

     # Method to enter the user's email ID   
     def useremailid(self, useremailid):
          self.user_email.click(timeout=0)
          self.user_email.fill(useremailid)

     # Method to click the "Next" button after entering the email
     def nextemail(self):
          self.next_button.click(timeout=0)

     # Method to enter the user's email password
     def useremailpassword(self, useremailpassword):
          self.user_emailpassword.click(timeout=0)
          self.user_emailpassword.fill(useremailpassword)
          
     # Method to click the "Next" button after entering the email passwor
     def nextpasswordbutton(self):
          self.page.wait_for_timeout(2000)
          self.nextpassword_button.click(timeout=0)
          self.page.wait_for_timeout(10000)
          
     # Method to fill in Google login page details
     def fill_googlelink_loginpage_details(self):
  
     # Enter "Student details"
          self.user_name.fill("qateststudentabh10")
     # Click on "Google "
          self.googleloginbutton()
     # Enter the "Email ID"
          self.user_email.fill("namratayashwant.k@fevtutor.com")
     # Click on "Next" Button
          self.nextemail()       
     # Enter the "User's Password"   
          self.user_emailpassword.fill("Pass123")
          self.page.wait_for_timeout(5000)
     # Click on "Next" Button
          self.nextpasswordbutton()
          self.page.wait_for_timeout(5000)

     # after login it will redirect to home page
          return googleloginhomepage(self.page)
          

          
     
         

     

     