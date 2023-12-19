from playwright.sync_api import expect
from PageObjects.logout_page import logoutpage
from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import get_sessionhistory_download_path

class devtomhomepage:
      
      def __init__(self,page):
      # Initialize the devtom class with a Playwright page object
            self.page = page

      # Create an assertionandvalidation instance
            self.assert_validate = assertionandvalidation()
      
      # Elements on the page
            self.session_button = page.get_by_role("link", name="  Session")
            self.sessionHistory_button= page.get_by_role("link", name="Session History").first
            
                
      def fill_session_id_details(self):
      # Click on "Session"
            self.session_button.click(timeout=0)
      # Click on "Session History"
            with self.page.expect_popup() as sessionhistoryTab:
                 self.sessionHistory_button.click(timeout=0)
            Newtab =sessionhistoryTab.value
      # Click on "Subject"
            Newtab.locator("#txtSubject").click(timeout=0)
            
            self.page_heading = Newtab.get_by_role("heading", name="Session History", exact=True)
            expect(self.page_heading, "Session History page header mismatch").to_contain_text("Session History")


            while Newtab.locator("#divSessionIdHistorySearch",has_text="Session ID").is_visible() is False:
                 #Newtab.mouse.wheel(0,200)
                 Newtab.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            Newtab.locator("#txtsessionid").click(timeout=0)       
            
          
            # Enter the session ID
            searchSessionId = "11464109"
            Newtab.locator("#txtsessionid").fill(searchSessionId)
            self.assert_validate.sessionHistory_validate_sessionid(Newtab, searchSessionId)
            #click on "Search " Button            
            Newtab.locator("#MSessionSearch").click(timeout=0)

            # Scroll further down (you can adjust the scroll distance)
            Newtab.evaluate('window.scrollBy(0, 300);')
            self.page.wait_for_timeout(3000)
            # Scroll further down (you can adjust the scroll distance)
            Newtab.evaluate('window.scrollBy(0, 300);')
            
            # Locate the scrollable element with id="grdSessionHistroy"
            scrollable_element = Newtab.locator("#grdSessionHistroy")

            # Use JavaScript to scroll the scrollable element to the right by 300 pixels
            scrollable_element.evaluate('(element) => { element.scrollLeft += 300; }')


            with Newtab.expect_popup() as session_recording:
                  Newtab.get_by_role("link", name="View...").click()
            my_rec = session_recording.value
            my_rec.wait_for_load_state()
            
            # Validate session recording
            # Check if the title contains the expected text
            title = my_rec.title()
            expected_text = "11464109 | 6.EE.A.2.B.Working with Variables (Review) - 1"
            assert expected_text in title, f"Title mismatch. Expected: '{expected_text}', Actual: '{title}'"
            my_rec.close()

            # Click on "View Chat..." and close the popup
            with Newtab.expect_popup() as session_recording_chat:
                  Newtab.get_by_role("link", name="View Chat...").click()
            my_rec_chat = session_recording_chat.value
            my_rec_chat.wait_for_load_state()

            title = my_rec_chat.title()
            # Check if the title matches the expected text
            expected_text = "Chat Script"
            assert expected_text in title, f"Title mismatch. Expected: '{expected_text}', Actual: '{title}'"
            my_rec_chat.close()

            #self.assert_validate.sessionHistory_validate_searchresult(Newtab)
            self.assert_validate.sessionHistory_validate_searchresult(Newtab)

            # Click on "Export To Excel" Button
            with Newtab.expect_download() as download_info:
                  Newtab.locator("#btnMExportToExcel").click()
            download = download_info.value
            # Download file 
            downloadfile_path = get_sessionhistory_download_path()
            # save downloded file
            download.save_as(downloadfile_path)
            self.page.wait_for_timeout(5000)
            # Close Session History Page 
            Newtab.close()
            # Logout Devtom role
            return logoutpage(self.page)
            
