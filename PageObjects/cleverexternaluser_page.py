from PageObjects.logout_page import logoutpage

class Externalroles:

    def __init__(self, page):
        try:
            # Initialize the Externalroles class with a Playwright page object
            self.page = page

            # Expect a popup and retrieve elements within the popup
            with page.expect_popup() as new_external_role_info:
                self.district_admin_name = page.get_by_role("button", name="Log in as Stephanie Jones")
                self.teacher_name = page.get_by_role("button", name="Log in as Madyn  Abeles")
            
            new_external_role = new_external_role_info.value

            # Elements for external role navigation
            self.tutoring_schedule = new_external_role.get_by_role("link", name=" Tutoring Schedule")
            self.student_performance = new_external_role.get_by_role("link", name=" Student Performance Analysis")
            self.participation_points = new_external_role.get_by_role("link", name=" Participation Points")
            self.ext_session_history = new_external_role.get_by_role("link", name=" Session History")
            self.student_forum = new_external_role.get_by_role("link", name=" Student Forum")
            self.student_gamification = new_external_role.get_by_role("link", name="S Student Gamification Incentives")
            self.reports = new_external_role.get_by_role("link", name="  Reports")
            self.scholar = new_external_role.get_by_role("link", name="Print Scholar Cards")
            self.student_progress_report = new_external_role.get_by_role("link", name="Student Progress Report")
            self.district_progress_report = new_external_role.get_by_role("link", name="District Progress Report")
            self.nwea_testing_results = new_external_role.get_by_role("link", name="NWEA Testing Results")
            self.manage_student = new_external_role.get_by_role("link", name="  Manage Student Accounts")
            self.view_students = new_external_role.get_by_role("link", name="View Students")
            self.manage_user = new_external_role.get_by_role("link", name="  Manage User Accounts")
            self.view_user = new_external_role.get_by_role("link", name="View User")
            self.my_account = new_external_role.get_by_role("link", name=" My Account")
            self.new_ext_role_close = new_external_role
            self.banner = page.get_by_role("button", name="close modal window")
            self.custom_report = new_external_role.get_by_role("link", name="Custom Report- Individual Student")
            self.group_report = new_external_role.get_by_role("link", name="Student Group Report")
            self.edit_profile = new_external_role.get_by_role("link", name="Edit Profile")
            self.edit_settings = new_external_role.get_by_role("link", name="Edit Settings")
            self.sm_logout = new_external_role.get_by_role("link", name=" Logout")
            
        except:
            print("exception")

    def external_roles_navigation(self):
        # Click on various external role navigation links
        self.tutoring_schedule.click()
        self.student_performance.click()
        self.participation_points.click()
        self.ext_session_history.click()
        self.student_forum.click()
        self.student_gamification.click()
        self.reports.click()
        self.scholar.click()
        self.nwea_testing_results.click()
        self.manage_student.click()
        self.view_students.click()
        self.my_account.click()
            
    def district_admin_reports(self):
        # Click on various reports for district admin
        self.reports.click()
        self.student_progress_report.click()
        self.district_progress_report.click()
        self.manage_user.click()
        self.view_user.click() 

    def teacher_reports(self):
        # Click on various reports for teachers
        self.reports.click()
        self.custom_report.click()
        self.group_report.click()
        self.my_account.click()
        self.edit_profile.click()
        self.edit_settings.click()
    
    def external_users_logout(self):
        # Perform logout for external users
        self.sm_logout.click()
        self.new_ext_role_close.close()
        self.banner.click()

        # Return the logoutpage instance
        return logoutpage(self.page)
