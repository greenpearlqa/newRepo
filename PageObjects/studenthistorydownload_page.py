from PageObjects.logout_page import logoutpage
from Utilities.paths import download_excel_file_path


class studenthistorydownloadpage:

    def __init__(self, page):
        # Initialize the studenthistorydownloadpage class with a Playwright page object
        self.page= page

        # Elements on the page
        self.sessionHistory_button = page.get_by_role("link" , name=" Session History")
        self.AY_data= page.locator("#ddlDateRange")
        self.search_button= page.get_by_role("button", name="Search")
        self.download_button = page.get_by_role("button", name="Download")
        
    #Method to fill in student session history details and perform a download
    def fill_student_sessionHistory_details(self):
        # Click on the "Session History" button
        self.sessionHistory_button.click(timeout=0)
        self.page.wait_for_timeout(3000)
       
        # Select the Academic Year (AY)
        self.AY_data.select_option("2023")
        self.page.wait_for_timeout(1000)

        # Click on the "Search" button
        self.search_button.click(timeout=0)
        
        # Expect a download to start
        with self.page.expect_download() as download_info:
            self.page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
            self.download_button.click()

        # Get the downloaded file and save it       
        download_file = download_info.value
        download_file.save_as(download_excel_file_path())
        
        # Return to the logout page
        return logoutpage(self.page)
           

   