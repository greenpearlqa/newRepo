from Utilities.paths import get_bulk_plan_result_file

class BulkPlanSchedule:

    def __init__(self, page):
        # Initialize the BulkPlanSchedule class with a Playwright page object
        self.page = page

    def download_file(self):
        # Expect a file download and click on the download link
        with self.page.expect_download() as result_file:
            self.page.locator(".col-md-12 > .text-danger").click()
            download = result_file.value

            # Save the downloaded file to a specific path using get_bulk_plan_result_file()
            download.save_as(get_bulk_plan_result_file())
            self.page.wait_for_timeout(3000)
