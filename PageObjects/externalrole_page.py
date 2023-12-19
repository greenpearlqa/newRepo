from datetime import datetime
from Utilities.assertion_validation import assertionandvalidation
from Utilities.urlutils import Urlutils
from playwright.sync_api import expect

class ExternalRoles:

    def __init__(self, page):
        # Initialize the ExternalRoles class with a Playwright page object
        self.page = page
        self.assert_validate = assertionandvalidation()
        self.url_utils = Urlutils(page)
        # Page header
        self.page_header = page.locator('#page-header').locator('h2')

        # Elements on the page
        self.user_id = page.get_by_placeholder("User ID")
        self.password = page.get_by_placeholder("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.tutoring_schedule_link = page.get_by_role("link", name="Tutoring Schedule")
        self.student_performance_analysis_link = page.get_by_role("link", name="Student Performance Analysis")
        self.participation_points_link = page.get_by_role("link", name="Participation Points")
        self.session_history_link = page.get_by_role("link", name="Session History")
        self.student_forum_link = page.get_by_role("link", name="Student Forum")
        self.student_gamification_incentives_link =  page.get_by_role("link", name="Student Gamification Incentives")
        self.reports_link = page.get_by_role("link", name="Reports")
        self.custom_report_link = page.get_by_role("link", name="Custom Report- Individual Student")
        self.student_group_report_link = page.get_by_role("link", name="Student Group Report")
        self.testing_results_link = page.get_by_role("link", name="NWEA Testing Results")
        self.print_scholar_cards_link = page.get_by_role("link", name="Print Scholar Cards")
        self.manage_student_accounts_link = page.get_by_role("link", name="Manage Student Accounts")
        self.viewstudents_link = page.get_by_role("link", name="View Students")
        self.myaccount_link = page.get_by_role("link", name="My Account")
        self.edit_profile_link  =  page.get_by_role("link", name="Edit Profile")
        self.edit_settings_link = page.get_by_role("link", name="Edit Settings")
        self.logout_link = page.get_by_role("link", name="Logout")
        self.student_progress_report_link = page.get_by_role("link", name="Student Progress Report")
        self.program_progress_report_link =  page.get_by_role("link", name="Program Progress Report")
        self.school_progress_report_link = page.get_by_role("link", name="School Progress Report")
        self.manage_user_link = page.get_by_role("link", name="Manage User Accounts")
        self.viewuser_link = page.get_by_role("link", name="View User")
        self.district_progress_report_link = page.get_by_role("link", name="District Progress Report")
        self.network_progress_report_link = page.get_by_role("link", name="Network Progress Report")
        self.on_demand = page.get_by_role("link", name="Z On Demand Session")
        self.my_schedule = page.get_by_role("link", name=" My Schedule")
        self.session_history = page.get_by_role("link", name=" Session History")
        self.my_journey = page.get_by_role("link", name=" My Journey")
        self.my_progress_report = page.get_by_role("link", name=" My Progress Report")
        self.pre_post_assigment = page.get_by_role("link", name=" Pre & Post Test Assignments")
        self.account_and_profile = page.get_by_role("link", name=" My Account & Profile")
        self.my_learning_plan = page.get_by_role("link", name=" My Learning Plan")
        self.content_libraby = page.get_by_role("link", name=" Content Library")
        self.lms = page.get_by_role("link", name=" LMS")
        self.view_and_edit_profile = page.get_by_role("link", name=" View / Edit Profile")
        self.qa_session_details = page.get_by_role("link", name=" QA Session Detail")
        self.empty_session_report = page.get_by_role("link", name="Empty Session Report - Tutor Feedback")

    # Method for teacher login
    def teacher_login(self):
        self.user_id.fill("qatestteacher1")
        self.password.fill("123")
        self.click_loginbutton()

    # Method to launch a URL
    def launch_url(self, url):
        self.page.goto(url)

    # Method to click the login button
    # Method to click the login button
    def click_loginbutton(self):
        self.login_button.click(timeout=0)

    # Method to click the "Tutoring Schedule" link and validate the page
    def click_tutoringschedule(self):
        self.tutoring_schedule_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Tutoring Schedule')

    # Method to click the "Student Performance Analysis" link and validate the page
    def click_studentperformanceanalysis(self):
        self.student_performance_analysis_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Student Performance Analysis')

    # Method to click the "Participation Point Leaderboard" link and validate the page
    def click_participationpoints(self):
        self.participation_points_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Participation Points Leaderboard')

    # Method to click the "Session History" link and validate the page
    def click_sessionhistory(self):
        self.session_history_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Session History')

    # Method to click the "Student forum" link and validate the page
    def click_studentforum(self):
        self.student_forum_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Student Forum')

    # Method to click the "Student Gamification Incentives" link and validate the page
    def click_incentiveslink(self):
        self.student_gamification_incentives_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Student Gamification Incentives')

    # Method to click the "Reports" link
    def click_reportslink(self):
        self.reports_link.click(timeout=0)

    # Method to click the "Custom Report- Individual Student" link and validate the page
    def click_customreport(self):
        self.custom_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Custom Report- Individual Student')


    # Method to click the "Custom Report-Student Group" link and validate the page
    def click_studentgroup(self):
        self.student_group_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Custom Report- Student Group')

    # Method to click the "NWEA Testing Results" link and validate the page
    def click_testingresult(self):
        self.testing_results_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Students NWEA Testing Results')

    # Method to click the "Print Scholar cards" link and validate the page
    def click_scholarcards(self):
        self.print_scholar_cards_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Generate Scholar Cards')

    # Method to click the "Manage student Accounts" link 
    def click_managestudentaccounts(self):
        self.manage_student_accounts_link.click(timeout=0)

    # Method to click the "View Student" link and validate the page
    def click_viewstudents(self):
        self.viewstudents_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Manage Student Account')

    # Method to click the "My Account" link 
    def click_myaccount_teacher(self):
        self.myaccount_link.click(timeout=0)

    # Method to click the " Edit Profile" link and validate the page
    def click_myaccount(self):
        self.myaccount_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Edit Profile')
        
    def click_editprofile(self):
        self.edit_profile_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Edit Profile')

    # Method to click the "Edit Setting" link and validate the page
    def click_editsettings(self):
        self.edit_settings_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Edit Settings')

# Method to click the "logout" link 
    def click_logout(self):
        self.logout_link.click(timeout=0)

    def click_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def programadmin_login(self):
        self.user_id.fill("qatestpa3")
        self.password.fill("123")
        self.click_loginbutton()
    
    # Method to click the "Student Progress Report" link and validate the page
    def click_studentreport(self):
        self.student_progress_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Student Progress Report')
        
    def click_programreport(self):
        self.program_progress_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Program Progress Report')

    def schooladmin_login(self):
        self.user_id.fill("qatestsm2")
        self.password.fill("123")
        self.click_loginbutton()
    
    # Method to click the "Student NWEA" link and validate the page
    def click_school_testingresult(self):
        self.testing_results_link.click(timeout=0)
        try:
            expect(self.page_header).to_have_text("Students Nwea")

        except NameError:
            print("Students NWEA Testing Results page is not found")
    # Method to click the "School Progress Report" link and validate the page
    def click_schoolprogressreport(self):
        self.assert_validate.validate_external_roles(self.page_header, 'Students Nwea')
        
    def click_schoolprogressreport(self):
        self.school_progress_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'School Progress Report')       

    def click_manageuseraccounts(self):
        self.manage_user_link.click(timeout=0)

    def click_viewuser(self):
        self.viewuser_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'View Users')

    def districtadmin_login(self):
        self.user_id.fill("qatestda1")
        self.password.fill("123")
        self.click_loginbutton()
    # Method to click the "District Progress Report" link and validate the page
    def click_districtprogressreport(self):
        self.district_progress_report_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'District Progress Report')
        
    def click_viewuser_district(self):
        self.viewuser_link.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Manage Accounts')

    def networkadmin_login(self):
        self.user_id.fill("qatestna2")
        self.password.fill("123")
        self.click_loginbutton()

# Method to click the "Network Progress Report" link and validate the page
    def click_networkprogressreport(self):
        self.network_progress_report_link.click(timeout=0)
        
    # Method for teacher login
    def student_login(self):
        #self.url_utils.portal_launch()
        self.user_id.fill("FevQAStu2001")
        self.password.fill("Fev@2023")
        self.click_loginbutton()

    def on_demand_session(self):
        self.on_demand.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'On Demand Session')

    def my_schedule_click(self):
        self.my_schedule.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'My Schedule')

    def session_history_click(self):
        self.session_history.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Session History')

    def my_journey_click(self):
        self.my_journey.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'My Journey')

    def my_progress_report_click(self):
        self.my_progress_report.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'My Progress Report')

    def pre_post_assigment_click(self):
        self.pre_post_assigment.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Pre & Post Testing')

    def my_account_and_profile_click(self):
        self.account_and_profile.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'My Account')

    def my_learning_plan_click(self):
        self.my_learning_plan.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'My Learning Plan')

    # Method for tutor login
    def tutor_login(self):
        self.url_utils.portal_launch()
        self.user_id.fill("fevqamateletutor011")
        self.password.fill("Fev@123456")
        self.click_loginbutton()

    def content_libraby_button(self):
        with self.page.expect_popup() as content_lib:
                 self.content_libraby.click(timeout=0)
        Newtab = content_lib.value
        Newtab.close()
    
    def lms_click(self):
        self.lms.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'LMS')

    def empty_session_report_click(self):
        self.empty_session_report.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'Update Progress Reports')

    def view_and_edit_profile_click(self):
        self.view_and_edit_profile.click(timeout=0)
        self.assert_validate.validate_external_roles(self.page_header, 'View Profile')

    # Method for teacher login
    def otheradmin_login(self):
        self.user_id.fill("qatestoa4")
        self.password.fill("123")
        self.click_loginbutton()

  # Method to validate copyright information
    def validate_copyright(self):
        copyright_element = self.page.locator('.offCanvas .mb5')
        copyright_text = copyright_element.inner_text()
        current_year = str(datetime.now().year)
        expected_text = f"Copyrights ©{current_year} FEV Tutor. All rights reserved."

        if expected_text in copyright_text:
            print("Copyright information validated successfully!")
        else:
            print("Copyright information validation failed!")
