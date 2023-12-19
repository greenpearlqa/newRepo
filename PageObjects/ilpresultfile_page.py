# Import necessary modules and functions
from Utilities.paths import get_bulk_student_ilp_result
from Utilities.assertion_validation import assertionandvalidation

# Define the IlpResultFile class
class IlpResultFile:

    # Constructor for IlpResultFile, takes a 'page' parameter
    def __init__(self, page):
        self.page = page
        self.assert_validate = assertionandvalidation()

    # Method to download the ILP result file
    def download_result_file(self):
        # Expect a download and click the download link
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Bulk upload successful. Please click here to download the Result file.").click()
        
        # Get information about the downloaded file
        download = download_info.value
        
        # Define the download file path using a utility function
        downloadfilepath = get_bulk_student_ilp_result()
        
        # Save the downloaded file to the specified path
        download.save_as(downloadfilepath)
        
        # Validate the downloaded ILP result file
        self.assert_validate.validate_bulk_ilp_result_file_validation(self.page)
