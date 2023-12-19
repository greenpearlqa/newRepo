import time
from PageObjects.logout_page import logoutpage
from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import get_groupsession_upload_file_path
class groupsessionhomepage:
      
      def __init__(self,page):
            self.page = page
            self.assert_validate = assertionandvalidation()
            self.session_button = page.get_by_role("link", name="  Session")
            self.bulksessionschedule_button = page.get_by_role("link", name="Bulk Session Schedule", exact=True)
            # self.bulkSessionSchedule_link = page.goto("https://admin.fevtutor.com/ScheduleManager/ScheduleManager/BulkScheduleSession")
            self.browsandupload_button = page.get_by_text("Browse & Upload")
            self.file_path= get_groupsession_upload_file_path()
            self.submit_button = page.get_by_role("button", name="Submit")
            self.resultfile_link = page.get_by_role("link", name="Bulk upload successful. Please click here to download the Result file.")

      def sessionbutton(self):
            self.session_button.click(timeout=0)
            self.page.wait_for_timeout(1000)
            
      def bulksessionschedulebutton(self):
            self.bulksessionschedule_button.click(timeout=0)
            self.assert_validate.group_session_validate_bulkschedule_click(self.page)   
            self.page.wait_for_timeout(2000)

      def browseandupload(self):

            self.browsandupload_button.set_input_files(self.file_path, timeout=0)
            self.page.wait_for_timeout(2000)
            # self.assert_validate.validate_bulk_schedule_upload_file(self.page)
            
      def submitButton(self):
            self.submit_button.click(timeout=0)
            self.assert_validate.validate_bulk_schedule_upload_process(self.page)

      def fill_groupsession_file_details(self):
            self.browseandupload()
            self.submitButton()
            self.page.wait_for_timeout(10000)
            