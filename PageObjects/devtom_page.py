from playwright.sync_api import expect
from Utilities.assertion_validation import assertionandvalidation
class OperationalManager:

    def __init__(self, page):
        self.page=page
        #Session menu pages
        self.livesession= page.get_by_role("link", name="Live Sessions")
        self.boardactivity= page.get_by_role("link", name="Board Activity")
        self.session2= page.get_by_role("link", name="Sessions", exact=True)
        self.sessionstatus= page.get_by_role("link", name="Session Status")
        self.publishstudentcomment= page.get_by_role("link", name="Publish Student Comments")
        self.addtutorfeedback= page.get_by_role("link", name="Add Tutor Feedback for Completed Session(s)")
        self.tutorfocusreview= page.get_by_role("link", name="Tutor Focus Review")
        self.sessionassign= page.get_by_role("link", name="Session Assign")
        self.transferongoing= page.get_by_role("link", name="Transfer on-going session")
        self.sessionunassign= page.get_by_role("link", name="Session Unassign")
        self.holdsession= page.get_by_role("link", name="Hold Session Auto Cancellation")
        self.groupsessioncreation= page.get_by_role("link", name="Group Session Creation")

        #School menu pages
        self.viewschoolglobal= page.get_by_role("link", name="View School Global")
        self.viewprogramglobal= page.get_by_role("link", name="View Programs Global")
        self.addnewlms= page.get_by_role("link", name="Add new LMS", exact=True)
        self.viewlms= page.get_by_role("link", name="View LMS", exact=True)
        self.managecourse= page.get_by_role("link", name="Manage Course")
        self.viewschedule= page.get_by_role("link", name="View Schedule Student List")

        #Tutoring menu pages
        self.tutoring= page.get_by_role("link", name="  Tutoring")
        self.addnewtutor= page.get_by_role("link", name="Add New Tutor")
        self.viewtutor= page.get_by_role("link", name="View Tutor List")
        self.viewtutoravailablity= page.get_by_role("link", name="View Tutor Availability")
        self.viewworkpool= page.get_by_role("link", name="View Workpool")
        self.addworkpool= page.get_by_role("link", name="Add Workpool")
        self.tutorworkpoolmap= page.get_by_role("link", name="Tutor-Workpool Mapping")
        self.tutorteammap= page.get_by_role("link", name="Tutor-Team Mapping")
        self.teamleadismap= page.get_by_role("link", name="TeamLead-IS Mapping")
        self.managetutorcenter= page.get_by_role("link", name="Manage Tutoring Center")
        self.addtutorcenter= page.get_by_role("link", name="Add Tutoring Center Manager")
        self.viewtutorcenter= page.get_by_role("link", name="View Tutoring Center Managers")
        self.tutortimeslot= page.get_by_role("link", name="Tutor Timeslot")
        self.resetgauth= page.get_by_role("link", name="Reset GAuth")
        self.tutorblaclist= page.get_by_role("link", name="Tutor BlackList")
        self.bucketlist= page.get_by_role("link", name="BucketList Tutor View")
        self.tutorwhitelist= page.get_by_role("link", name="Tutor White List")
        self.publishsessiondata= page.get_by_role("link", name="Published Session Data")

        #Bulk Operations menu pages
        self.bulkoperation= page.get_by_role("link", name="  Bulk Operations")
        self.tutorregistration= page.get_by_role("link", name="Tutor Registration")
        self.billablestatus= page.get_by_role("link", name="Billable Status")
        self.bulkplanschedule= page.get_by_role("link", name="Bulk Plan Schedule", exact=True)
        self.bulkplandelete= page.get_by_role("link", name="Bulk Plan Delete", exact=True)
        self.bulkondemandsession= page.get_by_role("link", name="Bulk On-Demand Session Creation", exact=True)
        self.bulkpreferredetutor= page.get_by_role("link", name="Bulk Preferred Tutor Assigning To Sessions")
        self.createbulkother= page.get_by_role("link", name="Create Bulk Other Admin(s)")
        self.updatelesson= page.get_by_role("link", name="Update Lesson Reference")
        self.bulkblacklistadd= page.get_by_role("link", name="BulkTutor BlackList Add")
        self.bulkblacklistupdate= page.get_by_role("link", name="BulkTutor BlackList Update")
        self.bulktutorwhitelist= page.get_by_role("link", name="Bulk Tutor WhiteList")

        #Report menu pages
        self.reports= page.get_by_role("link", name="  Reports")
        self.tsaprogressreport= page.get_by_role("link", name="TSA Progress Report")
        self.managesummaryreport= page.get_by_role("link", name="Manage Summary Report")
        self.viewsummaryreport= page.get_by_role("link", name="View Summary Report")
        self.bulksummaryreport= page.get_by_role("link", name="Bulk Summary Report")

        #ilp menu pages
        self.ilp= page.get_by_role("link", name="  ILP")
        self.studentilp= page.get_by_role("link", name="Student ILP", exact=True)
        self.bulkilpwithbulkstudent= page.get_by_role("link", name="Bulk ILP with Bulk Students", exact=True)
        self.bulkilpwithbulkstudentnew= page.get_by_role("link", name="Bulk ILP with Bulk Students New")
        self.bulkilpwithprivatepaystudent= page.get_by_role("link", name="Bulk ILP with Bulk PrivatePay Students")
        self.viewlesson= page.get_by_role("link", name="View Lessons")
        self.addlesson= page.get_by_role("link", name="Add Lessons")
        self.addnewilpbucket= page.get_by_role("link", name="Add New ILP Bucket")
        self.viewilpbucket= page.get_by_role("link", name="View ILP Buckets")
        self.ilpharddelete= page.get_by_role("link", name="ILPs Hard Delete")
        
        #Manage network district and user menu pages
        self.managenetwork= page.get_by_role("link", name="Manage Networks")
        self.addinternaluser= page.get_by_role("link", name="Add Internal User")
        self.viewinternaluser= page.get_by_role("link", name="View Internal User")
        self.addqualityanalyst= page.get_by_role("link", name="Add Quality Analyst")
        self.qualityanalyst= page.get_by_role("link", name="Quality Analyst List")

        #Other menu pages
        self.other= page.get_by_role("link", name="  Others")
        self.managegrade= page.get_by_role("link", name="Manage Grade")
        self.managesubject= page.get_by_role("link", name="Manage Subject")
        self.editprofile= page.get_by_role("link", name="Edit Profile")
        self.studentbillinfo= page.get_by_role("link", name="Student Billing Info")
        self.managecurriculamhire= page.get_by_role("link", name="Manage Curriculam Hirearchy")
        self.viewuserlogreport= page.get_by_role("link", name="View User Log Report")
        self.bulkcurriculamstructurelevel= page.get_by_role("link", name="Bulk Curriculum Structure and Level")
        self.programspecificinputform= page.get_by_role("link", name="Program Specific Input Form")

        #NWEA menu pages
        self.nwea= page.get_by_role("link", name="  NWEA")
        self.createilpimportresult= page.get_by_role("link", name="Create ILP by Importing Results")
        self.nweatestresult= page.get_by_role("link", name="NWEA Test Result")
        self.bulkstudentnweabidmap= page.get_by_role("link", name="Bulk Student-NweaBid Mapping")
        self.bulkilprequest= page.get_by_role("link", name="Bulk ILP Request", exact=True)
        self.bulkilplessondelte= page.get_by_role("link", name="Bulk ILP Lesson Delete", exact=True)
        self.nweamapilpdownload= page.get_by_role("link", name="NWEA Map Testbased ILP Download")
        self.reviewbulkilplessondelete= page.get_by_role("link", name="Review Bulk ILP Lesson Delete")
        self.bulkilplessonsort= page.get_by_role("link", name="Bulk ILP Lesson Sorting")
        self.downloadilpnweastudent= page.get_by_role("link", name="Download ILP for NWEA Student")    
        
        #missed session pages
        self.missedsession= page.get_by_role("link", name=" Missed Sessions")
        self.missedunassignedsession= page.get_by_role("link", name=" Missed UnAsiggned Sessions")

        #Revert bucket to workpoll
        self.revertbuckettoworkpoll= page.get_by_role("link", name="Revert Bucket to Workpool")

        self.valid1= assertionandvalidation()
        self.locators= self.valid1.adminpagevalidationpageheader(page)
        self.locators2= self.valid1.adminpagevalidationwrapper(page)

        
    def session_menu(self, page):
        self.boardactivity.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Board Activity Report")
        
        self.session2.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Sessions")
        
        self.sessionstatus.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Update Session Status")
        
        self.publishstudentcomment.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Publish Comments")
        
        self.addtutorfeedback.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Session Tutor Feedback Report")
        
        self.tutorfocusreview.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Focus Review")
       
        self.sessionassign.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Session Assign")
        
        self.transferongoing.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Transfer on-going session")
       
        self.sessionunassign.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Session Unassign")
        
        self.holdsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Disable Session Auto Cancellation")
        
        self.groupsessioncreation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Create Group Session")
        
        

    def session_menuremaining(self, page):
        self.livesession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Live Sessions")
        
        # with page.expect_popup() as qasessiondetails_info:
        #     self.qasessiondetails= page.get_by_role("link", name="QA Session Detail")
        #     self.qasessiondetails.click()
        #     page.wait_for_timeout(24000)
        #     popup_page= qasessiondetails_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         expect(self.locators).to_have_text("QA Session Details")

        #     except Exception as NameError:
        #         print("Qa session details page is not found")
        # popup_page.close()
        


    def school_menu(self,page):
        #self.viewschoolglobal(timeout=0)
        #page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("")

        # except Exception as NameError:
        #     print(" page is not found")
        #self.viewprogramglobal.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("")

        # except Exception as NameError:
        #     print(" page is not found")
        self.addnewlms.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add LMS")
        
        self.viewlms.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View LMS")
        
        self.managecourse.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "Add Course")
        

        self.viewschedule.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Students")


    def tutoring_menu(self, page):
        self.tutoring.click(timeout=0)
        page.wait_for_timeout(3000)
        self.addnewtutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Tutor")
       
        self.viewtutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Tutors")
        
        self.viewtutoravailablity.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Availability")
        
        self.viewworkpool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Workpools")
        
        self.addworkpool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Workpool")
       
        self.tutorworkpoolmap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add / Remove Tutor to WorkPool")
       
        self.tutorteammap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add / Remove Teams")
       
        self.teamleadismap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add / Remove Tutor TeamLead to IS")
       
        self.managetutorcenter.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Tutoring Center")
        
        self.addtutorcenter.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Tutoring Center Manager")
        
        self.viewtutorcenter.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View TutoringCenter Managers")
        
        self.tutortimeslot.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Time Slot")
       
        self.resetgauth.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Reset Google Auth")
        
        self.tutorblaclist.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor BlackList")
        
        self.bucketlist.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View TutorBucketList")
        
        self.tutorwhitelist.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor WhiteList")
        
        self.publishsessiondata.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Published Session Data")
        

    def bulkoperation_page(self, page):
        self.bulkoperation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.tutorregistration.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Registration")
        
        self.billablestatus.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Billable-Status")
        
        self.bulkplanschedule.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Schedule")
        
        self.bulkplandelete.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
        
        self.bulkondemandsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk On-demand Session Creation")
        
        self.bulkpreferredetutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Preferred Tutor Assign To Sessions")
        
        self.createbulkother.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Other Admin-Registration")
        
        self.updatelesson.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Update Lesson Reference")
        
        self.bulkblacklistadd.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk TutorBlackList Add")
        
        self.bulkblacklistupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk TutorBlackList Update")
        
        self.bulktutorwhitelist.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Tutor WhiteList")
        


    def reports_menu(self, page):
        self.reports.click(timeout=0)
        page.wait_for_timeout(3000)
        self.tsaprogressreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "TSA Log Report")
        
        page.wait_for_timeout(3000)
        
        with page.expect_popup() as studentprogressreport_info:
            self.studentprogressreport= page.get_by_role("link", name="Student Progress Report")
            self.studentprogressreport.click()
            page.wait_for_timeout(12000)
            popup_page= studentprogressreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Student Progress Reports")
            
        
        popup_page.close()

        with page.expect_popup() as attendancereport_info:
            self.attendancereport= page.get_by_role("link", name="Attendance Report")
            self.attendancereport.click()
            page.wait_for_timeout(12000)
            popup_page= attendancereport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Attendance Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        self.managesummaryreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Summary Report Mail")
        
        self.viewsummaryreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Summary Report Mail")
        
        self.bulksummaryreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Summary Report Mail Bulk Upload")
        

        with page.expect_popup() as preferredtutor_info:
            self.preferredtutorreport= page.get_by_role("link", name="Preferred Tutor Report", exact=True)
            self.preferredtutorreport.click()
            page.wait_for_timeout(12000)
            popup_page= preferredtutor_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Preferred Tutor Report")
            
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as studentuniquetutorsessionreport_info:
            self.studentuniquereport= page.get_by_role("link", name="Students Unique Tutors Sessions Report")
            self.studentuniquereport.click()
            page.wait_for_timeout(12000)
            popup_page= studentuniquetutorsessionreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Students Unique Tutors Sessions Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as tutortimeslotreport_info:
            self.tutortimeslotreport= page.get_by_role("link", name="Tutor Time Slot Report")
            self.tutortimeslotreport.click()
            page.wait_for_timeout(12000)
            popup_page= tutortimeslotreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor Time Slot Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as assignedtutorreport_info:
            self.assigntutorreport= page.get_by_role("link", name="Assigned Tutor Report")
            self.assigntutorreport.click()
            page.wait_for_timeout(12000)
            popup_page= assignedtutorreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="wrapper"]/div/div/div/div/h2')
            self.valid1.validate_internal_roles(locators, "Assigned Tutor Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as assignedsessionpick_info:
            self.assignedsessionvspickedreport=  page.get_by_role("link", name="AssignedSessionsVSPicked Report")
            self.assignedsessionvspickedreport.click()
            page.wait_for_timeout(12000)
            popup_page= assignedsessionpick_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="wrapper"]/div/div/div/div/h2')
            self.valid1.validate_internal_roles(locators, "SessionsAssignedVSPicked Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as tutorreporttom_info:
            self.tutorreporttom= page.get_by_role("link", name="Tutor Report-TOM")
            self.tutorreporttom.click()
            page.wait_for_timeout(12000)
            popup_page= tutorreporttom_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as tutorstudentreport_info:
            self.tutorstudentreport= page.get_by_role("link", name="Tutor/Student Report")
            self.tutorstudentreport.click()
            page.wait_for_timeout(12000)
            popup_page= tutorstudentreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="wrapper"]/div/div/div/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor/Student Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as preferredstudenttutorreport_info:
            self.preferstudenttutorreport= page.get_by_role("link", name="Preferred Student-Tutor Report")
            self.preferstudenttutorreport.click()
            page.wait_for_timeout(12000)
            popup_page= preferredstudenttutorreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="wrapper"]/div/div/div/div/h2')
            self.valid1.validate_internal_roles(locators, "Preferred Student - Tutor Report")
            
                
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as tutorofflinereport_info:
            self.tutorofflinereport= page.get_by_role("link", name="Tutor Offline Report")
            self.tutorofflinereport.click()
            page.wait_for_timeout(12000)
            popup_page= tutorofflinereport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor Offline Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as missedsessionreport_info:
            self.missedsessionreport= page.get_by_role("link", name="Missed Session Report")
            self.missedsessionreport.click()
            page.wait_for_timeout(12000)
            popup_page= missedsessionreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Missed Sessions")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as preferredtutorreporttom_info:
            self.prefertutorreporttom= page.get_by_role("link", name="Preferred Tutor Report TOM")
            self.prefertutorreporttom.click()
            page.wait_for_timeout(12000)
            popup_page= preferredtutorreporttom_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="wrapper"]/div/div/div/div/h2')
            self.valid1.validate_internal_roles(locators, "Preferred Tutor Report")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as livetutorstatusreport_info:
            self.livetutorstatusreport= page.get_by_role("link", name="Live Tutor Status Report")
            self.livetutorstatusreport.click()
            page.wait_for_timeout(12000)
            popup_page= livetutorstatusreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Live Tutor Status")
            popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as tutortoteacheralert_info:
            self.tutortoteacheralert= page.get_by_role("link", name="Tutor To Teacher Alert")
            self.tutortoteacheralert.click()
            page.wait_for_timeout(12000)
            popup_page= tutortoteacheralert_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor To Teacher Alert")
        popup_page.close()
        page.wait_for_timeout(3000)

        # with page.expect_popup() as tlfeedbackcount_info:
        #     self.tlfeedbackcount= page.get_by_role("link", name="TL Feedback Count")
        #     self.tlfeedbackcount.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= tlfeedbackcount_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         locators= popup_page.locator('//*[@id="page-header"]/div/h2')
        #         expect(locators).to_have_text("")

        #     except Exception as NameError:
        #         print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)

        # page.wait_for_timeout(3000)

        # with page.expect_popup() as tlreport_info:
        #     self.tlreport= page.get_by_role("link", name="TL Report")
        #     self.tlreport.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= tlreport_info.value
        #     popup_page.wait_for_load_state("networkidle")
        # try:
        #     self.page= page
        #     locators= page.locator('//*[@id="page-header"]/div/h2')
        #     expect(locators).to_have_text("")

        # except Exception as NameError:
        #     print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)

        # with page.expect_popup() as schoolreport_info:
        #     self.schoolreport= page.get_by_role("link", name="School Report")
        #     self.schoolreport.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= schoolreport_info.value
        #     popup_page.wait_for_load_state("networkidle")
        # try:
        #     self.page= page
        #     locators= page.locator('//*[@id="page-header"]/div/h2')
        #     expect(locators).to_have_text("")

        # except Exception as NameError:
        #     print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000

        # with page.expect_popup() as qaanalystreport_info:
        #     self.qaanalystreport= page.get_by_role("link", name="QA Analyst Report").click()
        #     self.qaanalystreport.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= qaanalystreport_info.value
        #     popup_page.wait_for_load_state("networkidle")
        # try:
        #     self.page= page
        #     locators= page.locator('//*[@id="page-header"]/div/h2')
        #     expect(locators).to_have_text("")

        # except Exception as NameError:
        #     print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)

    def ilp_menu(self, page):
        self.ilp.click(timeout=0)
        page.wait_for_timeout(3000)   
        self.studentilp.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student Personal Training Plan")
        

        self.viewlesson.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Lessons")
        
        self.addlesson.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Custom Lesson")
        

    def ilp_menuremaining(self, page):
        
        self.bulkilpwithbulkstudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk - Student ILP Lesson Creation")
        
        self.bulkilpwithbulkstudentnew.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk - Student ILP Lesson Creation New")
        
        self.bulkilpwithprivatepaystudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk - Private Pay Student ILP Lesson Creation")
        
        
        self.addnewilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "ILP Bucket")
        
        self.viewilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View ILPBuckets")
        
        self.ilpharddelete.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student ILP(s) Hard Delete")
        

        page.wait_for_timeout(3000)

        with page.expect_popup() as emptyreportstudentilp_info:
            self.emptyreportstudentilp= page.get_by_role("link", name="Empty Report - Student ILP")
            self.emptyreportstudentilp.click()
            page.wait_for_timeout(12000)
            popup_page= emptyreportstudentilp_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Empty Report - Student ILP")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as ilpdownload_info:
            self.ilpdownload= page.get_by_role("link", name="ILP Download")
            self.ilpdownload.click()
            page.wait_for_timeout(12000)
            popup_page= ilpdownload_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Download ILP")
        popup_page.close()
        page.wait_for_timeout(3000)

    def managenduser_menu(self, page):
        self.managenetwork.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "Add/Modify Network")
        
        self.addinternaluser.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add User")
        
        self.viewinternaluser.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Users")
        

    def managenduser_menuremaining(self, page):
        self.addqualityanalyst.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Quality Analyst")
        
        self.qualityanalyst.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View All Quality Analyst")
        

    def other_menu(self, page):
        self.other.click(timeout=0)
        page.wait_for_timeout(3000)

        # with page.expect_popup() as qaroutine_info:
        #     self.qaroutine= page.get_by_role("link", name="QA Routine")
        #     self.qaroutine.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= qaroutine_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         locators= page.locator('//*[@id="page-header"]/div/h2')
        #         expect(locators).to_have_text("")

        #     except Exception as NameError:
        #         print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)

        self.managegrade.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Grade")
        
        self.managesubject.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Subjects")
        
        self.editprofile.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Edit Profile")
        
        
        with page.expect_popup() as viewacitivitylog_info:
            self.viewactivitylog= page.get_by_role("link", name="View Activity Log")
            self.viewactivitylog.click()
            page.wait_for_timeout(12000)
            popup_page= viewacitivitylog_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Activity Logs")
        popup_page.close()
        page.wait_for_timeout(3000)

        with page.expect_popup() as viewscheduleplan_info:
            self.viewscheduleplan= page.get_by_role("link", name="View Schedule Plan")
            self.viewscheduleplan.click()
            page.wait_for_timeout(12000)
            popup_page= viewscheduleplan_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Schedule Plans")
        popup_page.close()
        page.wait_for_timeout(3000)
    
        # self.studentbillinfo.click(timeout=0)
        # try:
        #     expect(self.locators).to_have_text("Student Billing Information")

        # except Exception as NameError:
        #     print("Student Billing Information page is not found")
        # page.wait_for_timeout(3000)
        self.managecurriculamhire.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Curriculam Hierarchy")
        
        self.viewuserlogreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View User Log Report")
        
        self.bulkcurriculamstructurelevel.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk School Curriculam Structure")
        

        # with page.expect_popup() as qareportdownload_info:
        #     self.qareportdownload= page.get_by_role("link", name="QA Report Download")
        #     self.qareportdownload.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= qareportdownload_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         locators= popup_page.locator('//*[@id="page-header"]/div/h2')
        #         expect(locators).to_have_text("")

        #     except Exception as NameError:
        #         print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)
        self.programspecificinputform.click(timeout=0)
        page.wait_for_timeout(3000)
        try:
            self.page= page
            locators= page.locator('//*[@id="Page-header"]/div/h2')
            expect(locators).to_have_text("Program Specific Input Form")

        except Exception as NameError:
            print("Program Specific Input Form page is not found")

    def nwea_menu(self, page):
        self.nwea.click(timeout=0)
        page.wait_for_timeout(3000)
        self.createilpimportresult.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Create ILP by Importing Results")
        
        self.nweatestresult.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "NWEA Test Result")
        
        self.bulkstudentnweabidmap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student-NweaBid")
       

        with page.expect_popup() as nweaschoollist_info:
            self.nweaschoollist= page.get_by_role("link", name="NWEA School List")
            self.nweaschoollist.click()
            page.wait_for_timeout(12000)
            popup_page= nweaschoollist_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Nwea Schools")
        popup_page.close()
        page.wait_for_timeout(3000)

        self.bulkilprequest.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "NWEA MAP Test Based ILP Preparation")
        
        self.bulkilplessondelte.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student ILP Lesson(s) Delete")
       
        self.nweamapilpdownload.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "NWE Map Test Based ILP Download")
        
        self.reviewbulkilplessondelete.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student ILP Lesson(s) Delete")
        
        self.bulkilplessonsort.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student ILP Lesson(s) Sorting")
        
        self.downloadilpnweastudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Download ILP for Student")
        

        # with page.expect_popup() as redflagsession_info:
        #     self.redflagsession= page.get_by_role("link", name=" Red Flagged Sessions")
        #     self.redflagsession.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= redflagsession_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         locators= popup_page.locator('//*[@id="page-header"]/div/h2')
        #         expect(locators).to_have_text("")

        #     except Exception as NameError:
        #         print(" page is not found")
        # popup_page.close()
        # page.wait_for_timeout(3000)

    def missedsession_menu(self, page):
        self.missedsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "TSA Missed Session")
        
        self.missedunassignedsession.click(timeout=3000)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "TSA Missed Session")
        
    def revertbucket_menu(self, page):
        self.revertbuckettoworkpoll.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Revert Bucket Ids to Workpool For Already Published Sessions")
        