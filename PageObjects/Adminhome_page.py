# Import necessary modules and specific page objects
from PageObjects.Adminschedule_page import Adminsessionpage
from PageObjects.Bulkplanschedule_page import BulkPlanSchedule
from Utilities.paths import download_OverlapBulkplanfile_path, download_bulkplan_publish_file, get_bulk_plan_nonrecurring_file, get_bulk_plan_recurring_file, get_bulkplan_regression_file, get_bulk_plan_upload_file, get_bulk_plan_with_pgm_upload_file
from Utilities.assertion_validation import assertionandvalidation

# Define the AdminHomepage class
class AdminHomepage:
    
    # Constructor for AdminHomepage, takes a 'page' parameter
    def __init__(self, page):
        self.page = page
        self.assert_validate = assertionandvalidation()
        
        # Define page elements (links, buttons, etc.)
        self.my_dashboard = page.get_by_role("link", name="Index - FEVTUTOR")
        self.school = page.get_by_role("link", name="School")
        self.devse_school = page.get_by_role("link", name="  School")
        self.dashboard = page.get_by_role("link", name="Dashboard")
        self.session = page.get_by_role("link", name="  Session")
        self.browse_upload = page.get_by_text("Browse & Upload")
        
        self.bulk_updation = page.get_by_role("link", name="  Bulk-Updation")
        
        self.bulkplanschedule = page.get_by_role("link", name="Bulk Plan Schedule")
        self.submit = page.get_by_role("button", name="Submit")
        
        
        self.ilppage = page.get_by_role("link", name="  ILP")
        self.ilpurl = page.get_by_role("link", name="Bulk ILP with Bulk Students New")
    
        # Devtom role
        self.devtom_bulk_updation = page.get_by_role("link", name="  Bulk Operations")
        self.devtom_browse_upload= page.get_by_label("Browse & Upload")
    # Click on the "School" link and return an Adminsessionpage object
    def click_on_school(self):
        self.school.click(timeout=0)
        return Adminsessionpage(self.page)
    
    # Click on the "Bulk-Updation" link and navigate to the "Bulk Plan Schedule" page
    # Perform file upload and return a BulkPlanSchedule object
    def click_on_bulkupdation(self):
        self.bulk_updation.click(timeout=0)
        self.bulkplanschedule.click()
        
        self.browse_upload.set_input_files(get_bulk_plan_upload_file())
        self.submit.click()
        self.page.wait_for_timeout(5000)
        # self.assert_validate.bulk_plan_schedule_validate_header(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfilelink(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfile()
        # self.browse_upload.set_input_files(get_bulk_paln_upload_file())
        # self.submit.click(timeout=0)
        return BulkPlanSchedule(self.page)
    
    # Click on the "ILP" link and navigate to the ILP creation page
    def click_on_ilpcreation(self):
        self.ilppage.click(timeout=0)
        self.ilpurl.click(timeout=0)
        self.assert_validate.validate_bulk_ilp_session_page(self.page)

    def click_on_bulkupdation_excel(self):
        #self.bulk_updation.click(timeout=0)
        #self.bulkplanschedule.click()
        self.browse_upload.set_input_files(get_bulk_plan_upload_file())
        self.submit.click()
        # self.assert_validate.bulk_plan_schedule_validate_header(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfilelink(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfile()
        # self.browse_upload.set_input_files(get_bulk_paln_upload_file())
        # self.submit.click(timeout=0)
        return BulkPlanSchedule(self.page)

    # Click on the "School" link in devse role dashboard and return an Adminsessionpage object
    def click_on_school_dashboard(self):
        self.devse_school.click(timeout=0)
        return Adminsessionpage(self.page)
    
    def Download_bulkplan_file(self):
        #self.bulk_updation.click(timeout=0)
        #self.bulkplanschedule.click()
        
        self.browse_upload.set_input_files(get_bulk_plan_upload_file())
        self.submit.click()
        self.page.wait_for_timeout(8000)
        # self.assert_validate.bulk_plan_schedule_validate_header(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfilelink(self.page)
        # self.assert_validate.bulk_plan_schedule_validate_downloadfile()
        # self.browse_upload.set_input_files(get_bulk_paln_upload_file())
        # self.submit.click(timeout=0)
        with self.page.expect_download() as download_info:
                
                self.page.locator(".col-md-12 > .text-danger").click()
        download_file = download_info.value
        download_file.save_as(download_OverlapBulkplanfile_path())
        self.page.wait_for_timeout(8000)
        self.assert_validate.overlap_bulkplan_result_file_validation()

        return BulkPlanSchedule(self.page)
    
    def click_on_bulkupdation_with_pgm_excel(self):
        self.browse_upload.set_input_files(get_bulk_plan_with_pgm_upload_file())
        self.submit.click()
        return BulkPlanSchedule(self.page)
    
    def select_bulk_recurring_plan(self):
        self.browse_upload.set_input_files(get_bulk_plan_recurring_file())
        self.submit.click()
        return BulkPlanSchedule(self.page)
    
    def select_bulk_nonrecurring_plan(self):
        self.browse_upload.set_input_files(get_bulk_plan_nonrecurring_file())
        self.submit.click()
        return BulkPlanSchedule(self.page)
    
    def devtom_bulkplanschedule(self):
                                    
        self.devtom_bulk_updation.click(timeout=0)
        self.bulkplanschedule.click(timeout=0)
        self.devtom_browse_upload.set_input_files(get_bulkplan_regression_file())
        self.submit.click(timeout=0)
        self.page.wait_for_timeout(5000)

    def devtom_download_bulkplanfile(self):

        with self.page.expect_download() as download_info:
                
                self.page.locator(".col-md-12 > .text-danger").click()
        download_file = download_info.value
        download_file.save_as(download_bulkplan_publish_file())
        self.page.wait_for_timeout(10000)
        #self.assert_validate.no_sessionoverlap_bulkplanpublish_file_validation()
        #self.assert_validate.overlap_bulkplan_result_file_validation()




