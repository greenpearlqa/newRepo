from Utilities.paths import get_bulk_ondemandsession_file_path


class BulkOnDemandScheduleFile:

    def __init__(self, page):
        # Initialize the Publishsession class with a Playwright page object
        self.page = page
        with page.expect_popup() as bulkondemand_info:
            page.get_by_role("link", name="Bulk On-Demand Session Creation")
        session_info = bulkondemand_info.value
        self.browseandupload_button = session_info.get_by_text("Browse & Upload")
        self.file_path= get_bulk_ondemandsession_file_path()
        self.submit_button = session_info.get_by_role("button", name="Submit")
    
    def browseandupload(self):
        self.browseandupload_button.set_input_files(self.file_path, timeout=0)
        self.page.wait_for_timeout(2000)
        
    def submitButton(self):
        self.submit_button.click(timeout=0)
