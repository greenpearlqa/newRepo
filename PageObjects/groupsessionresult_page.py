from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import get_groupsession_result_path

class Groupsessionresult:
       
    def __init__(self, page):
            # Initialize the GroupSessionResult class with a Playwright page object
            self.page = page

            # Create an assertion and validation instance
            self.assert_validate = assertionandvalidation()

            # Expect a download link for the result file
            with page.expect_download() as result_file:
                page.get_by_role("link", name="Bulk upload successful. Please click here to download the Result file.").click()
            
            # Get the downloaded file
            download = result_file.value

            # Define the file path where the result will be saved
            downloadfilepath = get_groupsession_result_path()

            # Save the downloaded result file
            download.save_as(downloadfilepath)

            # Validate the bulk schedule download result
            self.assert_validate.validate_bulk_schedule_download_result()