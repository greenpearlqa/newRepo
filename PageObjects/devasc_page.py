from Utilities.assertion_validation import assertionandvalidation
class AcademicSuccessCoach:

    def __init__(self, page):
        self.page=page
        #Es tracker page
        self.estracker= page.get_by_role("link", name="^ ES Tracker")

        #Session menu page
        self.oacsessionhistory= page.get_by_role("link", name="OAC-Session History Report")

        #view tutor page
        self.tutor= page.get_by_role("link", name="  Tutors")
        self.viewtutor= page.get_by_role("link", name="View Tutor")

        #Manage scholl menu pages
        self.manageschool= page.get_by_role("link", name="  Manage Schools")
        self.addschool= page.get_by_role("link", name="Add School")
        self.viewschool= page.get_by_role("link", name="View Schools")
        self.addprogram= page.get_by_role("link", name="Add Program")
        self.viewprogram= page.get_by_role("link", name="View Programs", exact=True)
        self.addsinglestudent= page.get_by_role("link", name="Add Single Student")
        self.addbulkstudent= page.get_by_role("link", name="Add Bulk Student")
        self.addcurriculam= page.get_by_role("link", name="Add Curriculum Structure")
        self.managecurriculam= page.get_by_role("link", name="Manage School Curriculum Levels")
        self.addbulkstudent= page.get_by_role("link", name="Add Bulk Student")
        self.studentdetailsview= page.get_by_role("link", name="Student detail view", exact=True)

        #Other pages
        self.managegrade= page.get_by_role("link", name="Manage Grade")
        self.managesubject= page.get_by_role("link", name="Manage Subject")
        self.managecourse= page.get_by_role("link", name=" Manage Course")
        self.document= page.get_by_role("link", name=" Documents")

        #Utilization report menu pages
        self.utilization= page.get_by_role("link", name="  Utilization Report")
        self.schoolreport= page.get_by_role("link", name="School Report")
        self.programreport= page.get_by_role("link", name="Program Report")

        #Report menu pages
        self.report= page.get_by_role("link", name=" \">  Reports")
        self.customreportindividualstudent= page.get_by_role("link", name="Custom Report - Individual Student", exact=True)
        self.customreportstudentgroup= page.get_by_role("link", name="Custom Report - Student Group", exact=True)
        self.studentuniquetutorsession= page.get_by_role("link", name="Student Unique Tutors Session")
        self.attendancereport= page.get_by_role("link", name="Attendance Report")

        #send report menu pages
        self.sendreport= page.get_by_role("link", name="  Send Report")
        self.individualstudentanalysisreport= page.get_by_role("link", name="Individual Student Analysis Report", exact=True)
        self.leaderboard= page.get_by_role("link", name="Leader Board", exact=True)
        self.attendancesummaryreport= page.get_by_role("link", name="Attendance Summary Report", exact=True)
        self.weeklyprogressreport= page.get_by_role("link", name="Weekly Progress Report", exact=True)

        #Lesson and learning plan menu pages
        self.lessonlearningplan= page.get_by_role("link", name="  Lessons and Learning Plans")
        self.studentlearningplan= page.get_by_role("link", name="Student Learning Plan")
        self.viewlesson= page.get_by_role("link", name="View Lessons")
        self.addlesson= page.get_by_role("link", name="Add New Lesson")
        self.ilpbucket= page.get_by_role("link", name="ILP Bucket", exact=True)
        self.viewilpbucket= page.get_by_role("link", name="View ILP Buckets")

        #quality assurance menu pages
        self.qualityassurance= page.get_by_role("link", name="  Quality Assurance")
        self.dashboard= page.get_by_role("link", name="Dashboard", exact=True)
        self.sessiondetails= page.get_by_role("link", name="Session Detail")
        self.analystlist= page.get_by_role("link", name="Analyst List")
        self.mailbox= page.get_by_role("link", name="Mailbox")

        self.valid1= assertionandvalidation()
        self.locators= self.valid1.adminpagevalidationpageheader(page)
        self.locators2= self.valid1.adminpagevalidationwrapper(page)
        self.locators4= self.valid1.adminpagevalidationmyheader(page)
        self.locators6= self.valid1.adminpagevalidationpageheaders(page)

    def estracker_page(self, page):
        self.estracker.click(timeout=0)
        page.wait_for_timeout(3000)

    def session_menu(self, page):
        # self.oacsessionhistory.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     self.page= page
        #     locators= page.locator('//*[@id="page-header"]/div/h2')
        #     expect(locators).to_have_text("Create Group Session")

        # except Exception as NameError:
        #     print("Create Group Session page is not found")

        with page.expect_popup() as sessionhistory_info:
            self.sessionhistory= page.get_by_role("link", name="Session History", exact=True)
            self.sessionhistory.click()
            page.wait_for_timeout(12000)
            popup_page= sessionhistory_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Session History")
        popup_page.close()

    def tutor_menu(self, page):
        self.tutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.viewtutor.click(timeout=0)
        self.valid1.validate_internal_roles(self.locators, "View Tutors")

    def manageschool_menu(self,page):

        self.manageschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.addschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add School")
        self.viewschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View School")
        self.addprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Program")
        self.viewprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Programs")

        self.addsinglestudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Student")

        self.addcurriculam.click(timeout=0)
        page.wait_for_timeout(3000)
 
        self.valid1.validate_internal_roles(self.locators4, "Add Curriculum Structure")
        
        self.managecurriculam.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Manange School Curriculum Levels")

        self.studentdetailsview.click()
        page.wait_for_timeout(3000)
        locators= page.locator('//*[@id="page-header"]/div/div[1]/div/h2')
        self.valid1.validate_internal_roles(locators, "Student Search")

        self.addbulkstudent.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student Bulk Registration")

    def other_menu(self, page):
        self.managegrade.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Grade")
        
        self.managesubject.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Subjects")

        self.managecourse.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Add Course")

        self.document.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Document")
    
    def utilization_menu(self, page):
        self.utilization.click(timeout=0)
        page.wait_for_timeout(6000)

        with page.expect_popup() as teacherreport_info:
            self.teacherreport= page.get_by_role("link", name="Teacher Report")
            self.teacherreport.click()
            page.wait_for_timeout(12000)
            popup_page= teacherreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Teacher Utilization Report")
        popup_page.close()
        
        self.schoolreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "School Utilization Report")

        self.programreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Program Utilization Report")

    def report_menu(self, page):
        self.report.click(timeout=0)
        page.wait_for_timeout(3000)
        self.customreportindividualstudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Custom Report- Individual Student")

        self.customreportstudentgroup.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Custom Report- Student Group")

        with page.expect_popup() as transactiondetail_info:
            self.transactiondetails= page.get_by_role("link", name="Transaction Details")
            self.transactiondetails.click()
            page.wait_for_timeout(12000)
            popup_page= transactiondetail_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Transaction Details")
        popup_page.close()

        with page.expect_popup() as tutorreporttom_info:
            self.tutorreporttom= page.get_by_role("link", name="Tutor Report-TOM")
            self.tutorreporttom.click()
            page.wait_for_timeout(12000)
            popup_page= tutorreporttom_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor Report")
        popup_page.close()

    def report_menuremaining(self, page):
        with page.expect_popup() as tutortoteacheralert_info:
            self.tutorteacheralert= page.get_by_role("link", name="Tutor To Teacher Alert")
            self.tutorteacheralert.click()
            page.wait_for_timeout(12000)
            popup_page= tutortoteacheralert_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor To Teacher Alert")
        popup_page.close()

        self.studentuniquetutorsession.click(timeout=0)
        page.wait_for_timeout(3000)
        locators= popup_page.locator('//*[@id="Page-header"]/div[1]/h2')
        self.valid1.validate_internal_roles(locators, "Students Unique Tutors Sessions Report")

    def sendreport_menu(self, page):
        self.sendreport.click()
        page.wait_for_timeout(3000)
        self.individualstudentanalysisreport.click(timeout=0)
        page.wait_for_timeout(6000)
        self.valid1.validate_internal_roles(self.locators, "Analysis Report")

        self.leaderboard.click(timeout=0)
        page.wait_for_timeout(6000)
        self.valid1.validate_internal_roles(self.locators6, "Leadership Report")
            
    def sendreport_menuremaining(self, page):
        self.attendancesummaryreport.click(timeout=0)
        page.wait_for_timeout(6000)
        self.valid1.validate_internal_roles(self.locators6, "Attendance Report")

        # self.weeklyprogressreport.click(timeout=0)
        # page.wait_for_timeout(6000)
        # try:
        #     expect(self.locators6).to_have_text("Attendance Report")

        # except Exception as NameError:
        #     print("Attendance Report page is not found")

    
    def lessonlearningplan_menu(self, page):
        self.lessonlearningplan.click()
        self.viewlesson.click(timeout=0)
        self.studentlearningplan.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Student Personal Training Plan")

        self.viewlesson.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "View Lessons")
        
        self.addlesson.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "Manage Custom Lesson")
        
        self.ilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "ILP Bucket")

        self.viewilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators6, "View ILPBuckets")

    def qualityassurance_menu(self, page):
        self.qualityassurance.click()
        page.wait_for_timeout(3000)
        self.dashboard.click(timeout=0)
        page.wait_for_timeout(16000)
        self.valid1.validate_internal_roles(self.locators6, "Dashboard")

        self.sessiondetails.click(timeout=0)
        page.wait_for_timeout(14000)
        self.valid1.validate_internal_roles(self.locators6, "QA Session Details")

        self.analystlist.click(timeout=0)
        page.wait_for_timeout(14000)
        self.valid1.validate_internal_roles(self.locators6, "View All Quality Analyst")

        # self.mailbox.click()
        page.wait_for_timeout(9000)




        