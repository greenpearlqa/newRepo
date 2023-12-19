import time


class Myprogressreport:

    def __init__(self,page):
        self.page = page
        page.get_by_role("link", name=" My Progress Report").click()
        page.locator("#ddlDateRange").select_option("1")
        page.get_by_role("button", name="Create Report").click()
        with page.expect_download() as download_info:
            page.get_by_role("button", name="Download").click()
        download = download_info.value
        page.on("dialog", lambda dialog: dialog.accept())
        time.sleep(12)
        page.get_by_role("link", name=" Logout").click()
