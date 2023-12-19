from playwright.sync_api import expect
from Utilities.assertion_validation import assertionandvalidation
class EngagementSpecilist:

    def __init__(self, page):
        self.page=page
        self.dashboardnew= page.get_by_role("link", name=" Dashboard New")
        self.programspecificmasterdata= page.get_by_role("link", name=" Program Specific Master Data")

        #session menu pages
        self.session= page.get_by_role("link", name="  Sessions")
        self.livesession= page.get_by_role("link", name="Live Sessions")

        #view tutor
        self.tutor=  page.get_by_role("link", name="  Tutors")
        self.viewtutor= page.get_by_role("link", name="View Tutor")

        #Manage network district and user menu pages
        self.managendu= page.get_by_role("link", name="  Manage Network District and User")
        self.managenetwork= page.get_by_role("link", name="Manage Networks")
        self.managedistrict= page.get_by_role("link", name="Manage Districts")
        self.adduser= page.get_by_role("link", name="Add User")
        self.viewuser= page.get_by_role("link", name="View User", exact=True)

        #Manage scholl menu pages
        self.manageschool= page.get_by_role("link", name="  Manage Schools")
        self.viewschool= page.get_by_role("link", name="View Schools")
        self.viewprogram= page.get_by_role("link", name="View Programs", exact=True)
        self.studentdetailsview= page.get_by_role("link", name="Student detail view", exact=True)

        #Report menu pages
        self.report= page.get_by_role("link", name=" \">  Reports")
        self.customreportindividualstudent= page.get_by_role("link", name="Custom Report - Individual Student", exact=True)
        self.customreportstudentgroup= page.get_by_role("link", name="Custom Report - Student Group", exact=True)
        self.attendancereport= page.get_by_role("link", name="Attendance Report")

        #send report menu pages
        self.sendreport= page.get_by_role("link", name="  Send Report")

        #Lesson and learning plan
        self.lessonlearningplans= page.get_by_role("link", name="  Lessons and Learning Plans")
        self.studentlearningplan= page.get_by_role("link", name="Student Learning Plan")
        self.viewlesson= page.get_by_role("link", name="View Lessons")
        self.addlesson= page.get_by_role("link", name="Add New Lesson")
        self.ilpbucket= page.get_by_role("link", name="ILP Bucket", exact=True)
        self.viewilpbucket= page.get_by_role("link", name="View ILP Buckets", exact=True)

        self.valid1= assertionandvalidation()
        self.locators= self.valid1.adminpagevalidationpageheader(page)
        self.locators2= self.valid1.adminpagevalidationwrapper(page)
        self.locators4= self.valid1.adminpagevalidationmyheader(page)
        self.locators6= self.valid1.adminpagevalidationpageheader(page)

    def dashboardprogram_page(self, page):
        self.dashboardnew.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "ES Dashboard")

        self.programspecificmasterdata.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Program Specific Master Data")

    def session_menu(self, page):
        self.livesession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Live Sessions")

    def tutor_menu(self, page):
        self.tutor.click()
        page.wait_for_timeout(3000)
        self.viewtutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "View Tutors")

    def managenduser_menu(self, page):
        self.managenetwork.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "Add/Modify Network")

        # self.adduser.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("Add User")

        # except Exception as NameError:
        #     print("Add User page is not found")

    def manageschool_menu(self,page):

        self.manageschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.viewschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View School")

        self.viewprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Programs")

        self.studentdetailsview.click()
        page.wait_for_timeout(3000)
        self.page= page
        locators= page.locator('//*[@id="page-header"]/div/div[1]/div/h2')
        self.valid1.validate_internal_roles(locators, "Student Search")
    
    def report_menu(self, page):

        with page.expect_popup() as studentuniquetutorsession_info:
            self.studentuniquetutoreport= page.get_by_role("link", name="Student Unique Tutors Session", exact=True)
            self.studentuniquetutoreport.click()
            page.wait_for_timeout(12000)
            popup_page= studentuniquetutorsession_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Students Unique Tutors Sessions Report")
        popup_page.close()

    def sendreport_menu(self, page):
        self.sendreport.click()
        page.wait_for_timeout(3000)

        with page.expect_popup() as individualstudentanalysis_info:
            self.individualstudentanalysisshared= page.get_by_role("link", name="Individual Student Analysis shared")
            self.individualstudentanalysisshared.click()
            page.wait_for_timeout(12000)
            popup_page= individualstudentanalysis_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div[1]/h2')
            self.valid1.validate_internal_roles(locators, "Analysis Report")
        popup_page.close()

        with page.expect_popup() as leadershipboard_info:
            self.leadershipboard= page.get_by_role("link", name="Leadership Board")
            self.leadershipboard.click()
            page.wait_for_timeout(12000)
            popup_page= leadershipboard_info.value
            popup_page.wait_for_load_state("networkidle")
            locators = popup_page.locator('//*[@id="page-header"]/div[1]/h2')
            self.valid1.validate_internal_roles(locators, "Leadership Report")
        popup_page.close()

        with page.expect_popup() as attendancesummaryreport_info:
            self.attendancesummaryreport= page.get_by_role("link", name="Attendance Summary Report")
            self.attendancesummaryreport.click()
            page.wait_for_timeout(12000)
            popup_page= attendancesummaryreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(self.locators6, "Attendance Report")
        popup_page.close()


        with page.expect_popup() as weeklyprogressreport_info:
            self.weeklyprogressreport= page.get_by_role("link", name="Weekly Progress Report")
            self.weeklyprogressreport.click()
            page.wait_for_timeout(12000)
            popup_page= weeklyprogressreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div[1]/h2')
            self.valid1.validate_internal_roles(locators, "Weekly Progress Report")
        popup_page.close()

    def lessonlearningilp_menu(self, page):
        self.lessonlearningplans.click()
        page.wait_for_timeout(3000)
        self.studentlearningplan.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Student Personal Training Plan")

        self.viewlesson.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "View Lessons")

        self.addlesson.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Manage Custom Lesson")

        self.ilpbucket.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "ILP Bucket")

        self.viewilpbucket.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "View ILPBuckets")