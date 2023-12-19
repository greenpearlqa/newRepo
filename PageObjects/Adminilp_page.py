from Utilities.paths import get_bulk_Student_ilp_upload
from Utilities.assertion_validation import assertionandvalidation

class AdminIlpPage: 

#devtom role navigating bulk ilp creation page, selecting the drop down field & browse and upload sample file
    def __init__(self, page):
        self.page= page
        self.assert_validate = assertionandvalidation()
        self.browse_upload = page.get_by_text("Browse & Upload")
        self.file_path = get_bulk_Student_ilp_upload()
        page.once("dialog", lambda dialog: dialog.accept())
        self.upload= page.get_by_role("button", name="Upload")
        page.once("dialog", lambda dialog: dialog.accept())
        self.submit= page.get_by_role("button", name="Submit")     

#Action for browse and upload sample file
    def browse_and_upload(self):
        self.browse_upload.set_input_files(self.file_path)
        self.upload.click(timeout=0)
        self.assert_validate.validate_bulk_ilp_uploadfile(self.page)
        self.submit.click(timeout=0)
        self.assert_validate.validate_bulk_ilp_upload_process(self.page)



    