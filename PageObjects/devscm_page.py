from Utilities.assertion_validation import assertionandvalidation

class ScheduleManager:

    def __init__(self, page):
        self.page=page
        #Session menu pages
        self.groupsessioncreation= page.get_by_role("link", name="Group Session Creation")
        self.sessionlist= page.get_by_role("link", name="Session List")
        self.publishsession= page.get_by_role("link", name="Published Sessions")
        self.bulksessionschedule= page.get_by_role("link", name="Bulk Session Schedule", exact=True)
        self.tempbulksessionschedulenew= page.get_by_role("link", name="Temp - Bulk Session Schedule New", exact=True)
        self.publishplanrepublishsession= page.get_by_role("link", name="Publish Plans / Re-Publish Sessions")

        #Ticket menu pages
        self.ticket= page.get_by_role("link", name="  Ticket")
        self.addticket= page.get_by_role("link", name="Add Ticket")
        self.viewsupportticket= page.get_by_role("link", name="View Support Ticket")

        #School menu pages
        self.viewprogram= page.get_by_role("link", name="View Programs List")
        self.swapteacher= page.get_by_role("link", name="Swap Teacher")
        self.assignteacherstudent= page.get_by_role("link", name="Assign Teacher To Student")
        self.publishstudentcomment= page.get_by_role("link", name="Publish Student Comments")
        self.bulkstudentteacherswap= page.get_by_role("link", name="Bulk Student Teacher Swapping")
        self.studentsessionprivilage= page.get_by_role("link", name="Student And Session Privileges")
        self.viewstudentpage= page.get_by_role("link", name="View Student List")

        #ilp menu pages
        self.addnewilpbucket= page.get_by_role("link", name="Add ILP Bucket")
        self.viewilpbucket= page.get_by_role("link", name="View ILPBuckets")

        #Tutoring menu pages
        self.tutoring= page.get_by_role("link", name="  Tutoring")
        self.tutoravailablity= page.get_by_role("link", name="Tutor Availability")
        self.tutortimeslot= page.get_by_role("link", name="Tutor Timeslot")
        self.bulktutorfeedbackupdate= page.get_by_role("link", name="Bulk Tutor-Feedback Updation", exact=True)
        self.bulkpreferredetutor= page.get_by_role("link", name="Bulk Prefered Tutor Assign To Sessions")

        #Remaining page
        self.managedepartment= page.get_by_role("link", name=" Manage Department")
        self.vieweditprofile=  page.get_by_role("link", name=" View / Edit Profile")
        self.bulkplanschedule= page.get_by_role("link", name=" Bulk Plan Schedule")
        self.bulkplandelete= page.get_by_role("link", name=" Bulk Plan Delete")
        self.bulkplanexclude= page.get_by_role("link", name=" Bulk Plan Excluding")
        self.bulksessiontagdetails= page.get_by_role("link", name=" Bulk Session Tag Details")
        self.bulkprogramswap= page.get_by_role("link", name="Bulk Program Swap")

        self.valid1= assertionandvalidation()
        self.locators= self.valid1.adminpagevalidationpageheader(page)
        self.locators2= self.valid1.adminpagevalidationwrapper(page)

    def session_menu(self, page):

        # self.groupsessioncreation.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     self.page= page
        #     locators= page.locator('//*[@id="page-header"]/div/h2')
        #     expect(locators).to_have_text("Create Group Session")

        # except Exception as NameError:
        #     print("Create Group Session page is not found")

        self.sessionlist.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Sessions")
        
        self.bulksessionschedule.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Schedule Sessions")
        

        self.tempbulksessionschedulenew.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Schedule Sessions")
        

        self.publishplanrepublishsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Publish/Re-Publish 1:1 Sessions")
        page.wait_for_timeout(3000)


        with page.expect_popup() as bulkondemandsessioncreation_info:
            self.bulkondemandsessioncreation= page.get_by_role("link", name="Bulk On-Demand Session Creation")
            self.bulkondemandsessioncreation.click()
            page.wait_for_timeout(12000)
            popup_page= bulkondemandsessioncreation_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Bulk On-demand Session Creation")
            popup_page.close()

    
    def ticket_menu(self, page):
        self.ticket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.addticket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Ticket")
       

        self.viewsupportticket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Tickets")

    
    def school_menu(self,page):                
        self.viewprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Programs")
       

        self.swapteacher.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Swap Teacher")
       

        self.assignteacherstudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Teacher To Student(s)")
        

        self.publishstudentcomment.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Publish Comments")
        

        self.bulkstudentteacherswap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student-Teacher Swapping")
        

        with page.expect_popup() as viewnotes_info:
            self.viewnotes= page.get_by_role("link", name="View Notes")
            self.viewnotes.click()
            page.wait_for_timeout(12000)
            popup_page= viewnotes_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Notes")
        popup_page.close()

        # self.viewstudentpage.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("Register Students")

        # except Exception as NameError:
        #     print("Register Students page is not found")


    def ilp_menu(self, page):
        self.addnewilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "ILP Bucket")
       
        self.viewilpbucket.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View ILPBuckets")
        


    def tutoring_menu(self, page):
        self.tutoring.click(timeout=0)
        page.wait_for_timeout(3000)
        self.tutoravailablity.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Availability")
        

        self.tutortimeslot.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Tutor Time Slot")
        

        self.bulktutorfeedbackupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Tutor-Feedback Updation")
       

        with page.expect_popup() as bulktutorfeedbackloghistory_info:
            self.bulktutorupdateloghistory= page.get_by_role("link", name="Bulk Tutor-Feedback Updation Log Histroy")
            self.bulktutorupdateloghistory.click()
            page.wait_for_timeout(12000)
            popup_page= bulktutorfeedbackloghistory_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Bulk Tutor Feedback Updation Log Histroy")
        popup_page.close()

        self.bulkpreferredetutor.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Preferred Tutor Assign To Sessions")
        
    
    def remaining_pages(self, page):
        self.managedepartment.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "ManageDepartment")
        

        self.vieweditprofile.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Edit Profile")
       

        self.bulkplanschedule.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Schedule")
       

        self.bulkplandelete.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
       

        self.bulkplanexclude.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
        

        self.bulksessiontagdetails.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Session Tag Details")
       

        self.bulkprogramswap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Program Swap")
        

        with page.expect_popup() as viewscheduleplan_info:
            self.viewscheduleplan= page.get_by_role("link", name=" View Schedule Plan")
            self.viewscheduleplan.click()
            page.wait_for_timeout(12000)
            popup_page= viewscheduleplan_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Schedule Plans")
            popup_page.close()

        with page.expect_popup() as studentuniquetutorsession_info:
            self.studentuniquetutorsessionreport= page.get_by_role("link", name=" Students Unique Tutors Sessions Report")
            self.studentuniquetutorsessionreport.click()
            page.wait_for_timeout(12000)
            popup_page= studentuniquetutorsession_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Students Unique Tutors Sessions Report")
        popup_page.close()


        with page.expect_popup() as tutorreporttom_info:
            self.tutorreport= page.get_by_role("link", name="Tutor Report-TOM")
            self.tutorreport.click()
            page.wait_for_timeout(12000)
            popup_page= tutorreporttom_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Tutor Report")
        popup_page.close()
        