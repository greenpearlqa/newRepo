import time

from PageObjects.whiteboard_page import whiteboardpage


class studentgroupsession:
      
      def __init__(self,page):
            self.page= page
            self.joinnow_button = page.locator("//div[@id='divJoinNow']")

      def wait_for_clickable(self, timeout=10):
        start_time = time.time()
        while time.time() - start_time < timeout:
            if self.joinnow_button.is_enabled():
                return True
            time.sleep(1)
        return False

      def dashboard(self):
             
             if self.wait_for_clickable():
                  self.joinnow_button.click(timeout=0)
                  print("Join Now button clicked successfully!")
             else:
                  print("Join Now button was not clickable within the given timeout.")
            #  return whiteboardpage(self.page)