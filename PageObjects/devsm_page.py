from Utilities.assertion_validation import assertionandvalidation
from playwright.sync_api import expect
class SupportManager:

    def __init__(self, page):
        # Initialize the SupportManager class with a Playwright page object
        self.page=page
        # Elements on the page
        self.bulkprogramsessionswap= page.get_by_role("link", name="Bulk Program Session Swap", exact=True)
        self.addbulkschoolalert= page.get_by_role("link", name="Add Bulk Schools For Alert")
        self.report= page.get_by_role("link", name=" \">  Reports")

        # Create an assertion and validation instance
        self.valid1= assertionandvalidation()
        # Get validation locators
        self.locators= self.valid1.adminpagevalidationpageheader(page)

    # Method to access the "Bulk Program Session Swap" menu and validate the page
    def bulkupdation_menu(self, page):
        self.bulkprogramsessionswap.click(timeout=0)
        page.wait_for_timeout(3000)
        try:
             # Validate the page title
            expect(self.locators).to_have_text("Program Session Maping")

        except Exception as NameError:
            print(" Bulk Program Session swap page is not found")
        self.valid1.validate_internal_roles(self.locators, "Program Session Maping")

    # Method to access the "Add Bulk Schools For Alert" menu and validate the page      

    def alert_menu(self, page):
        self.addbulkschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        try:
            # Validate the page title
            expect(self.locators).to_have_text("Add Bulk Schools For Alert")

        except Exception as NameError:
            print("Add Bulk Schools For Alert page is not found")
        self.valid1.validate_internal_roles(self.locators, "Add Bulk Schools For Alert")

    # Method to access the "Reports" menu
    def report_menu(self, page):
        self.report.click(timeout=0)
        page.wait_for_timeout(3000)
