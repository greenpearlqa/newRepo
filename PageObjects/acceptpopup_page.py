import time

class Acceptpopup:
    def __init__(self,page):
        page.once("dialog", lambda dialog: dialog.accept())
        self.schedulebutton = page.get_by_role("button", name="Schedule")

    def click_schedulebutton(self):
      time.sleep(5)  
      self.schedulebutton.click()
      time.sleep(5)
      