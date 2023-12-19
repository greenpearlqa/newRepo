class logoutpage:

    def __init__(self,page):
      # Initialize the logout page class with a Playwright page object
      self.page =page

      # Handle browser dialogs by accepting them
      page.on("dialog", lambda dialog: dialog.accept())

      # Elements on the page
      self.logout_button = page.get_by_role("link", name=" Logout")
      self.userclick = page.get_by_role("button", name=" Pachamuthu S ")
      self.cleverlogout = page.get_by_role("button", name="Log out")
      self.devtomlogout_button = page.get_by_role("link", name=" Logout")
      self.groupsession_logout = page.get_by_role("link", name=" Logout")
      self.googlelink_logout =  page.get_by_role("link", name=" Logout")
      self.student_logout = page.get_by_role("link", name=" Logout")
      self.bulk_ondemandsession_logout = page.get_by_role("link", name=" Logout")

   # Method to perform the logout action
    def logout(self):
       self.logout_button.click()
    
   # Method to perform Clever logout
    def clever_logout(self):
        self.userclick.click()
        self.cleverlogout.click()
      
   # Method to perform Devtom logout
    def devtom_logout(self):
       self.devtomlogout_button.click()

   # Method to perform logout from the group session page
    def groupsessionpage_logout(self):
       self.groupsession_logout.click()

   # Method to perform logout when using Google link
    def googlelinklogout_button(self):
       self.googlelink_logout.click()

   # Method to perform logout for students
    def studentlogout_button(self):
       self.student_logout.click()
    
   # Method to perform logout from the group session page
    def bulkondemandsession_logout(self):
       self.bulk_ondemandsession_logout.click()