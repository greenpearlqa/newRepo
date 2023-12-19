from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import download_RecNonrecurBulkplanfile_path
class Bulksessionpublish:

    def __init__(self, page):
        # Initialize the Bulksessionpublish class with a Playwright page object
        self.page = page
        self.assert_validate = assertionandvalidation()
        # Elements on the page
        self.session = page.get_by_role("link", name="  Session")
        self.bulksession = page.get_by_role("link", name="Bulk Session Publish", exact=True)
        self.school = page.locator("#ddlSchool")

        # Accept the dialog once it appears
        page.once("dialog", lambda dialog: dialog.accept())

        self.publishall = page.get_by_role("button", name="Publish All")
        self.download_link = page.get_by_role("link", name="Click Here To Download Result File")
        self.no_plan_found = page.locator('//div[@class="col-sm-6"]')

          
    def bulksessionpublish(self):
        # Click on session and bulk session publish links
        self.session.click()
        self.bulksession.click()

        # Select a school (assuming "222" is a school ID)
        self.school.select_option("18781")

        # Click on the "Publish All" button
        self.publishall.click()

        # Wait for a timeout (adjust as needed)
        self.page.wait_for_timeout(10000)

        # Check if the download link is present
        

        if self.download_link:
            # Download file
            with self.page.expect_download() as download_info:
                self.download_link.click()
            download_file = download_info.value
            download_file.save_as(download_RecNonrecurBulkplanfile_path())
            
            self.page.wait_for_timeout(8000)
            self.assert_validate.RecuNonrecur_bulkplanpublish_file_validation()
            self.page.wait_for_timeout(6000)
        else:
            # Check if "No plans found to publish" message is present
            no_plans_message_selector = '//div[@class="col-sm-6"]'
            no_plans_message = self.page.query_selector(no_plans_message_selector)

            if no_plans_message:
                print("No plans found to publish.")
            else:
                # Handle other scenarios if needed
                print("Unexpected scenario occurred.")


    