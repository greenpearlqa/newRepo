from playwright.sync_api import expect
from Utilities.assertion_validation import assertionandvalidation
class SupportExecutive:

    def __init__(self, page):
        self.page=page

        #Session menu page
        self.session= page.get_by_role("link", name="  Session")
        self.livesession= page.get_by_role("link", name="Live Sessions", exact=True)
        self.livesessionglobal= page.get_by_role("link", name="Live Sessions Global")
        self.kpidata= page.get_by_role("link", name="KPI Raw data", exact=True)
        self.editenotes= page.get_by_role("link", name="Edit Session Notes")
        self.dailysessionforecast= page.get_by_role("link", name="Daily Session Forecast", exact=True)
        self.dailysessionforecastnetwork= page.get_by_role("link", name="Daily Session Forecast With Network")
        self.dailysessionforcasttime=page.get_by_role("link", name="Daily Session Forecast With Time Slot")
        self.starvingsession= page.get_by_role("link", name="Straving Sessions")
        self.bulksessionpublish= page.get_by_role("link", name="Bulk Session Publish", exact=True)
        self.bulksessionpublishtime= page.get_by_role("link", name="Bulk Session Publish With Time Slot")
        self.deletecancelsession= page.get_by_role("link", name="Delete / Cancel Sessions")
        self.deletecancelsessionglobal= page.get_by_role("link", name="Delete/Cancel Sessions Global")
        self.oacsessionhistory= page.get_by_role("link", name="OAC-Session History Report")

        #Manage network district and user menu pages
        self.managendu= page.get_by_role("link", name="  Manage Network District and User")
        self.adduser= page.get_by_role("link", name="Add User", exact=True)
        self.viewuser= page.get_by_role("link", name="View User", exact=True)
        self.viewuserglobal= page.get_by_role("link", name="View User Global", exact=True)
        self.swaproles= page.get_by_role("link", name="Swap Roles")
        self.managenetwork= page.get_by_role("link", name="Manage Network", exact=True)
        self.managedistrict= page.get_by_role("link", name="Manage Districts")

        #Other menu page
        self.others= page.get_by_role("link", name="  Others")
        self.programspecificinputform= page.get_by_role("link", name="Program Specific Input Form")

        #School menu pages
        self.school= page.get_by_role("link", name="  School")
        self.addschool= page.get_by_role("link", name="Add School")
        self.viewschool= page.get_by_role("link", name="View School", exact=True)
        self.addprogram= page.get_by_role("link", name="Add Program")
        self.viewprogram= page.get_by_role("link", name="View Programs", exact=True)
        self.addsinglestudent= page.get_by_role("link", name="Add Single Student")
        self.addcurriculam= page.get_by_role("link", name="Add Curriculum Structure")
        self.managecurriculam= page.get_by_role("link", name="Manage School Curriculum Levels")
        self.studentsessionprivilage= page.get_by_role("link", name="Student And Session Privileges", exact=True)
        self.studentsessionprivilageglobal= page.get_by_role("link", name="Student And Session PrivilegesGlobal")
        self.addbulkstudent= page.get_by_role("link", name="Add Bulk Student")
        self.viewstudentpage= page.get_by_role("link", name="View Student List", exact=True)

        #Bulk updation menu pages
        self.bulkupdation= page.get_by_role("link", name="  Bulk-Updation")
        self.teacherbulkregister= page.get_by_role("link", name="Teacher Bulk Registration")
        self.bulkprivilageupdation= page.get_by_role("link", name="Bulk Privilages Updation")
        self.assignbulkstudentprogram= page.get_by_role("link", name="Assign Bulk Student-Program")
        self.bulkstudentprogramunmapping= page.get_by_role("link", name="Bulk Student-Program Un-Mapping")
        self.assignbulkstudentteachernmapping= page.get_by_role("link", name="Assign Bulk Student-Teacher 1-N Mapping")
        self.assignbulkstudentteachermapping= page.get_by_role("link", name="Assign Bulk Student-Teacher 1-1 Mapping")
        self.bulkindividualstudentteacherunmapping= page.get_by_role("link", name="Bulk Individual Student-Teacher UnMapping")
        self.bulkcombinedstudentteacherunmapping= page.get_by_role("link", name="Bulk Combined Student-Teacher UnMapping")
        self.assignbulkteacherprogram= page.get_by_role("link", name="Assign Bulk Teacher-Program")
        self.bulkstudentstatusupdation= page.get_by_role("link", name="Bulk Student-Status Updation", exact=True)
        self.bulkstudentstatusupdationglobal= page.get_by_role("link", name="Bulk Student-Status UpdationGlobal")
        self.bulkstudentinfoupdation= page.get_by_role("link", name="Bulk Student-Info Updation", exact=True)
        self.bulkstudentinfoupdationwithoutschool= page.get_by_role("link", name="Bulk Student-Info Updation (with out schools)")
        self.bulkplanschedule= page.get_by_role("link", name="Bulk Plan Schedule")
        self.bulkplandelete= page.get_by_role("link", name="Bulk Plan Delete", exact=True)
        self.bulkplandelteeglobal= page.get_by_role("link", name="Bulk Plan DeleteGlobal")
        self.assignteacher= page.get_by_role("link", name="Assign Teacher", exact=True)
        self.assignteacherschooladmin= page.get_by_role("link", name="Assign Teacher To School Administrator")
        self.assignschool= page.get_by_role("link", name="Assign School")
        self.swapteacher= page.get_by_role("link", name="Swap Teacher")
        self.bulkusernamepasswordupdate= page.get_by_role("link", name="Bulk UserName or PasswordUpdate")
        self.billablestatus= page.get_by_role("link", name="Billable Status")
        self.bulkschooldeslotstatus= page.get_by_role("link", name="Bulk School Deslot Status", exact=True)
        self.bulkschooldeslotstatusglobal= page.get_by_role("link", name="Bulk School Deslot StatusGlobal")
        self.downloadteacherstudent= page.get_by_role("link", name="Download Teacher-Student", exact=True)
        self.downloadteacherstudentglobal= page.get_by_role("link", name="Download Teacher-Student Global")
        self.addbulkprivateschoolstudentmin= page.get_by_role("link", name="Add Bulk Private School Student Minutes")
        self.bulkstudentteacherswap= page.get_by_role("link", name="Bulk Student Teacher Swapping")
        self.bulkprogramsessionswap= page.get_by_role("link", name="Bulk Program Session Swap", exact=True)
        self.bulkprogramsessionswapglobal= page.get_by_role("link", name="Bulk Program Session Swap Global")
        self.bulkstudentcoursemap= page.get_by_role("link", name="Bulk Student Course Mapping")
        self.bulkschoolhourlygoalupdation= page.get_by_role("link", name="Bulk School Hourly Goals Updation")
        self.addeditbulkschool= page.get_by_role("link", name="Add/Edit Bulk School")
        self.addeditbulkprogram= page.get_by_role("link", name="Add /Edit Bulk Program")
        self.editbulkuser= page.get_by_role("link", name="Edit Bulk Users")
        self.assignodprogramsession= page.get_by_role("link", name="Assingn OD Program to Session")
        self.bulkprogramswap= page.get_by_role("link", name="Bulk Program Swap")


        #Alert menu pages
        self.alert= page.get_by_role("link", name="  Alerts")
        self.puasestartalert= page.get_by_role("link", name="Pause Start Alerts")
        self.sendbulksmsivr= page.get_by_role("link", name="Send Bulk SMS And IVR")
        self.addbulkschoolalert= page.get_by_role("link", name="Add Bulk Schools For Alert")
        self.addvirtualschoolalert= page.get_by_role("link", name="Add Virtual School Alert")
        self.addbmschoolalert= page.get_by_role("link", name="Add B&M School Alert")
        self.viewvirtualschoolalert= page.get_by_role("link", name="View Virtual School Alert")
        self.viewbmschoolalert= page.get_by_role("link", name="View B&M School Alert")
        self.pausestartalert= page.get_by_role("link", name="Pause Start Alerts")
        self.sendbulksmsivr= page.get_by_role("link", name="Send Bulk SMS And IVR")

        #Reports menu pages
        self.report= page.get_by_role("link", name="  Reports")
        self.studentprogressreport= page.get_by_role("link", name="Student Progress Report")
        self.nertworkutilizationreport= page.get_by_role("link", name="Network Utilization Report")
        self.districtutilizationreport= page.get_by_role("link", name="District Utilization Report")
        self.programutilizationreport= page.get_by_role("link", name="Program Utilization Report")
        self.schoolutilizationreport= page.get_by_role("link", name="School Utilization Report")

        #Assessment menu pages
        self.assessment= page.get_by_role("link", name="  Assessment")
        self.assigntest= page.get_by_role("link", name="Assign Test")
        self.learnositytestdetails= page.get_by_role("link", name="View Learnosity Test Details", exact=True)
        self.learnositytestresults= page.get_by_role("link", name="View Learnosity Test Results", exact=True)

        #ilp menu pages
        self.ilp= page.get_by_role("link", name="  ILP")
        self.viewilp= page.get_by_role("link", name="View ILP")

        #Wallet menu pages
        self.wallet= page.get_by_role("link", name="  Wallet")
        self.addprivatepaystudentmin= page.get_by_role("link", name="Add Private Pay Student Minutes")
        self.addremovestudentmin= page.get_by_role("link", name="Add / Remove Student Minutes")
        self.addremovestudentminglobal= page.get_by_role("link", name="Add/Remove Student Minutes Global")
        self.custompackage= page.get_by_role("link", name="Custom Package")
        self.studentbillinginfo= page.get_by_role("link", name="Student Billing Info")
        self.bulkstudentwalletminupdate= page.get_by_role("link", name="Bulk Student Wallet Minutes Update")

        #empty report student/user timezone
        self.emptyreporttimezone= page.get_by_role("link", name=" Empty Report - Student/User Timezone")
        self.emptyreporttimezoneglobal= page.get_by_role("link", name=" EmptyReport-Student/User TimezoneGlobal")


        #remaining pages
        self.bulkplanexcluding= page.get_by_role("link", name=" Bulk Plan Excluding", exact=True)
        self.bulkplanexcludingglobal= page.get_by_role("link", name=" Bulk Plan Excluding Global")
        self.managesubject= page.get_by_role("link", name=" Manage Subjects")
        self.managecourse= page.get_by_role("link", name=" Manage Course")
        self.viewscheduleplanglobal= page.get_by_role("link", name=" View Schedule PlanGlobal")
        self.nweatestresult = page.get_by_role("link", name=" NWEA Test Result")
        self.document= page.get_by_role("link", name=" Documents")

        #Utilization report menu pages
        self.utilization= page.get_by_role("link", name="  Utilization Report")

        #Newfeature menu pages
        self.newfeature= page.get_by_role("link", name="  New Feature")
        self.viewstudentlist2= page.get_by_role("link", name="View Student List", exact=True)

        #document page
        self.document= page.get_by_role("link", name=" Documents")

        #classlink menu pages
        self.classlink= page.get_by_role("link", name="  Class Link")
        self.datasynclog= page.get_by_role("link", name="Data Sync Log")
        self.continioussynclog= page.get_by_role("link", name="Continuous Sync Log")
        self.newstudentaccounts= page.get_by_role("link", name="New Student Accounts")
        self.newuseraccounts= page.get_by_role("link", name="New User Accounts")
        self.newdistrictschool= page.get_by_role("link", name="New District/Schools")
        self.bulkschoolupdate= page.get_by_role("link", name="Bulk School Update")
        self.bulkstudentupdate= page.get_by_role("link", name="Bulk Student Update", exact=True)
        self.bulkstudentupdateglobal= page.get_by_role("link", name="Bulk Student Update Global")
        self.bulkuserupdate= page.get_by_role("link", name="Bulk User Update")
        self.initiatedatasync= page.get_by_role("link", name="Initiate Data Sync", exact=True)
        self.downloaddata= page.get_by_role("link", name="Download Data", exact=True)

        #Clever menu pages
        self.clever= page.get_by_role("link", name=" d Clever")
        self.datasynclog2= page.get_by_role("link", name="Data Sync Log")
        self.continioussynclog2= page.get_by_role("link", name="Continuous Sync Log")
        self.bulkuserupdate2= page.get_by_role("link", name="Bulk User Update")
        self.bulkstudentupdate2= page.get_by_role("link", name="Bulk Student Update", exact=True)
        self.bulkstudentupdateglobal2= page.get_by_role("link", name="Bulk Student Update Global")
        self.eventlogclever= page.get_by_role("link", name="Event Logs from Clever")
        self.downloaddata2= page.get_by_role("link", name="Download Data")
        self.newuseracccount2= page.get_by_role("link", name="New User Accounts", exact=True)
        self.newuseraccountglobal2= page.get_by_role("link", name="New User Accounts Global", exact=True)
        self.newdistrictschool2= page.get_by_role("link", name="New District/Schools", exact=True)
        self.newdistrictschoolglobal2= page.get_by_role("link", name="New District/SchoolsGlobal", exact=True)
        self.initiatedatasync2= page.get_by_role("link", name="Initiate Data Sync", exact=True)
        self.newstudentaccount2= page.get_by_role("link", name="New Student Accounts", exact=True)

        self.valid1= assertionandvalidation()
        self.locators= self.valid1.adminpagevalidationpageheader(page)
        self.locators2= self.valid1.adminpagevalidationwrapper(page)
        self.locators3= self.valid1.adminpagevalidationsessionpagename(page)
        self.locators4= self.valid1.adminpagevalidationmyheader(page)
        self.locators5= self.valid1.adminpagevalidationwrapperform(page)
        

    
    def session_menu(self, page):
        self.session.click(timeout=0)
        page.wait_for_timeout(3000)
        self.kpidata.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "KPI Raw Data")
        
        self.dailysessionforecast.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "DailyForeCast Session")

        
    def session_menu_live(self, page):
        self.livesession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Live Sessions")
        
        page.wait_for_timeout(3000)

        self.bulksessionpublish.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "DailyForeCast Session Publish")

        self.bulksessionpublishtime.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "DailyForeCast Session Publish")
        


        # self.deletecancelsessionglobal.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("Delete (or) Cancel Sessions")
        #     print("\n Delete and Cancel session global page is working fine")

        # except Exception as NameError:
        #     print("\n Delete (or) Cancel Sessions page is not found")

        # with page.expect_popup() as page1_info:
            
        #     self.qasessiondetails= page.get_by_role("link", name="QA Session Detail")
        #     self.qasessiondetails.click()
        #     page.wait_for_timeout(12000)
        #     popup_page= page1_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         expect(self.locators).to_have_text("QA Session Details")
        #         print("\n qa session details page is working fine")

        #     except Exception as NameError:
        #         print("\n QA Session Details page is not found")
        # popup_page.close()

    def session_menu3(self, page):
        self.dailysessionforcasttime.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "DailyForeCast Session")
        

    def session_menuedse(self, page):
        self.editenotes.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators3, "Edit Session Notes")
        

        self.dailysessionforecastnetwork.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "DailyForeCast Session")
        

        self.starvingsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Starving Session Details")
        
        
        self.deletecancelsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Delete (or) Cancel Sessions")
        

        with page.expect_popup() as emptysessionreport_info:
            self.emptysessionreporttutorfeedback= page.get_by_role("link", name="Empty Session Report - Tutor Feedback")
            self.emptysessionreporttutorfeedback.click()
            page.wait_for_timeout(12000)
            popup_page= emptysessionreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Update Progress Reports")
        popup_page.close()

    def managenduser_menuadduser(self, page):
        self.adduser.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add User")
        

    def managenduser_menu(self, page):
        self.managendu.click(timeout=0)
        page.wait_for_timeout(3000)
        
        self.viewuser.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Users")
        

        self.managedistrict.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add/Modify District")
        

    def managenduser_menuswapviewuser(self, page):
        # self.viewuserglobal.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("View Users")
        #     print("\n View user global page is working fine")

        # except Exception as NameError:
        #     print("\n View Users page is not found")

        self.swaproles.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Swap Role")
        
        page.wait_for_timeout(3000)

    def managenduser_menunetwork(self, page):
        self.managenetwork.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "Add/Modify Network")
        

    def other_menu(self, page):
        self.others.click(timeout=0)
        page.wait_for_timeout(3000)
        self.programspecificinputform.click(timeout=0)
        page.wait_for_timeout(3000)
        locator = page.locator('//*[@id="Page-header"]/div/h2')
        self.valid1.validate_internal_roles(locator, "Program Specific Input Form")
        
    
    def school_menu(self,page):
        self.school.click(timeout=0)
        page.wait_for_timeout(3000)
        self.studentsessionprivilage.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student And Session Privileges")
        

        # self.viewstudentpage.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("Register Students")
        #     print("\n View student page is working fine")

        # except Exception as NameError:
        #     print("\n view student page is not found")

    def school_menuschoolprogram(self, page):
        self.addschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add School")
        
        self.viewschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View School")
        
        self.addprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Program")
        

    def school_menucurriculum(self, page):
        self.viewprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Programs")
        

        self.addcurriculam.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators4, "Add Curriculum Structure")
        

        self.managecurriculam.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manange School Curriculum Levels")
       


    def school_menustudentsessionprivilage(self, page):
        self.studentsessionprivilageglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Student And Session Privileges")
        

    # def school_menuaddbulk(self, page):
    #     self.addbulkstudent.click(timeout=0)
    #     page.wait_for_timeout(3000)
    #     try:
    #         expect(self.locators).to_have_text("Student Bulk Registration")
    #         print("\n Add bulk student page is working fine")

    #     except Exception as NameError:
    #         print("\n Add bulk student page is not found")

    def bulkupdation_menu(self, page):
        self.bulkupdation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.bulkplanschedule.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Schedule")
        
        self.bulkplandelete.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")

        self.teacherbulkregister.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Teacher Bulk Registration")
        
        
        self.bulkprivilageupdation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Updation Privilages")
       

        self.assignbulkstudentprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Program Mapping")
        
        
        self.bulkstudentprogramunmapping.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Program Un-Mapping")
       
        
        self.assignbulkstudentteachernmapping.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Teacher Mapping")
        
            
        self.assignbulkstudentteachermapping.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Teacher Single Mapping")
        
        
        self.bulkindividualstudentteacherunmapping.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "UnMapp Student-Teacher Mapping")
        
        
        self.bulkcombinedstudentteacherunmapping.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Teacher Un-Mapping")
        
        
        self.assignbulkteacherprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Bulk Teacher-Program Mapping")
        
        
        self.bulkstudentstatusupdation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Status Updation")
        
        self.bulkstudentinfoupdation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student-Info Updation")
        

        self.bulkstudentinfoupdationwithoutschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student-Info Updation")
        
        self.assignteacher.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Teacher To Student(s)")
        
        self.assignschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Student(s) To School")
        

        self.swapteacher.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Swap Teacher")
        

        self.bulkusernamepasswordupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk UserName Password Update")
        

        self.downloadteacherstudent.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Download Teacher-Student Mapping")
       

        self.addbulkprivateschoolstudentmin.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add Bulk Private School Student Minutes")
        

        self.bulkstudentteacherswap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student-Teacher Swapping")
        
        self.bulkschoolhourlygoalupdation.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Update School Hourly Goals")
        

        self.addeditbulkschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Manage School")
        

        self.addeditbulkprogram.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Manage Program")
        
        self.editbulkuser.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Manage User")

    
    def bulkupdation_menuremaining(self, page):
        self.bulkstudentstatusupdationglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Status Updation")
        

        self.bulkplandelteeglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
       

        self.assignteacherschooladmin.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Teacher To SchoolManager")
        
        self.bulkschooldeslotstatus.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk School Deslot Activation")
        

        self.bulkschooldeslotstatusglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk School Deslot Activation")
        

        self.downloadteacherstudentglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Download Teacher-Student Mapping")
        

        # self.bulkprogramsessionswapglobal.click(timeout=0)
        # page.wait_for_timeout(3000)
        # try:
        #     expect(self.locators).to_have_text("Program Session Mapping")
       #      print("\n Bulk program session swap global page is working fine")

        # except Exception as NameError:
        #     print("\n Bulk Program Session swap page is not found")

        self.bulkstudentcoursemap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Course Mapping")
        
        self.assignodprogramsession.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Program - Session Mapping")
        

        self.bulkprogramswap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Program Swap")
        

        self.billablestatus.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Billable Status")
        

        self.bulkprogramsessionswap.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Program Session Mapping")
       

    
    def alert_menu(self, page):
        self.alert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.addvirtualschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Virtual School Alert")
       

        self.addbmschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "B&M School Alert")
       
       
        self.viewvirtualschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Virtual Alert List")
        

        self.viewbmschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View BMS Alert List")
        

        with page.expect_popup() as nexmosmsreport_info:
            self.nexosmsreport= page.get_by_role("link", name="Nexmo SMS Report")
            self.nexosmsreport.click()
            page.wait_for_timeout(12000)
            popup_page= nexmosmsreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="login"]/tbody/tr/td/table/tbody/tr[1]/td/div/h1')
            self.valid1.validate_internal_roles(locators, "Login")
            
        popup_page.close()
        

        self.pausestartalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Pause Start Alerts")
        

        self.sendbulksmsivr.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Send Bulk SMS And IVR")
        

    def alert_menuremaining(self, page):
        self.addbulkschoolalert.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Schools For Alert")
        

    def report_menu(self, page):
        self.report.click(timeout=0)
        page.wait_for_timeout(3000)

        self.nertworkutilizationreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Network Utilization Report")
        

        self.districtutilizationreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "District Utilization Report")
        

        self.schoolutilizationreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "School Utilization Report")
        

        self.programutilizationreport.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Program Utilization Report")
        

    def report_menuremaining(self, page):

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

        with page.expect_popup() as transactiondetails_info:
            self.transactiondetails= page.get_by_role("link", name="Transaction Details")
            self.transactiondetails.click()
            page.wait_for_timeout(12000)
            popup_page= transactiondetails_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Transaction Details")
           
        popup_page.close()

        with page.expect_popup() as studentindvidualanalysisreport_info:
            self.studentindividualanalysisreport= page.get_by_role("link", name="Student Individual Analysis Report")
            self.studentindividualanalysisreport.click()
            page.wait_for_timeout(12000)
            popup_page= studentindvidualanalysisreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Student Individual Analysis Reports")
            
        popup_page.close()

        with page.expect_popup() as studentuniquetutorsession_info:
            self.studentuniquetutorsessionreport= page.get_by_role("link", name="Students Unique Tutors Sessions Report")
            self.studentuniquetutorsessionreport.click()
            page.wait_for_timeout(12000)
            popup_page= studentuniquetutorsession_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="Page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Students Unique Tutors Sessions Report")
            
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

    def assessment_menu(self, page):
        self.assessment.click(timeout=0)
        page.wait_for_timeout(3000)
        self.assigntest.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Assign Test")
        
        
    def assessment_menuremaining(self, page):
        self.learnositytestdetails.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View Learnosity Tests")
        
       
        self.learnositytestresults.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators5, "View Learnosity Test Results")
        

    
    def ilp_menu(self, page):
        self.ilp.click(timeout=0)
        page.wait_for_timeout(3000)
        self.viewilp.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "View ILPBuckets")
        

    def wallet_menu(self, page):
        self.wallet.click(timeout=0)
        page.wait_for_timeout(3000)
        self.addprivatepaystudentmin.click(timeout=0)
        page.wait_for_timeout(3000)
        locators= page.locator('//*[@id="dyn_0"]/div[2]/div/div[1]/div/div/div[1]/label')
        self.valid1.validate_internal_roles(locators, "Student ID :")

        self.addremovestudentmin.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add / Remove Student Minutes")
        
        self.addremovestudentminglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Add / Remove Student Minutes")
        

        self.custompackage.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Select Student")
        

        self.studentbillinginfo.click(timeout=0)
        page.wait_for_timeout(3000)
        locators= page.locator('//*[@id="dyn_0"]/div[2]/div/div[2]/div/div/div[1]/label')
        self.valid1.validate_internal_roles(locators, "Student ID :")\

        self.bulkstudentwalletminupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Student Wallet Minutes Update")
        

    def emptyreporttimezone_menu(self, page):
        self.emptyreporttimezone.click()
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Empty Report Student/User TimeZone")
       

    def emptyreporttimezone_menuglobal(self, page):
        self.emptyreporttimezoneglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Empty Report Student/User TimeZone")
        

    
    def remaning_page(self, page):
        self.bulkplanexcluding.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
        

        self.managesubject.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Manage Subjects")
        
        self.managecourse.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators2, "Add Course")
        

        with page.expect_popup() as viewactivitylog_info:
            self.viewactivitylog= page.get_by_role("link", name=" View Activity Logs")
            self.viewactivitylog.click()
            page.wait_for_timeout(12000)
            popup_page= viewactivitylog_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Activity Logs")
            
        popup_page.close()

        with page.expect_popup() as viewscheduleplan_info:
            self.viewscheduleplan= page.get_by_role("link", name=" View Schedule Plan", exact=True)
            self.viewscheduleplan.click()
            page.wait_for_timeout(12000)
            popup_page= viewscheduleplan_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "View Schedule Plans")
            
        popup_page.close()

        self.document.click(timeout=0)
        page.wait_for_timeout(3000)
        try:
            self.page= page
            expect(self.locators).to_have_text("Document")
            print("\n Document page is working fine")

        except Exception as NameError:
            print("\n Document page is not found")


    def remaing_pages(self, page):
        self.bulkplanexcludingglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Plan Delete")
        

        with page.expect_popup() as generatescholarcard_info:
            self.genaratescholarcards= page.get_by_role("link", name=" Generate Scholar Cards")
            self.genaratescholarcards.click()
            page.wait_for_timeout(12000)
            popup_page= generatescholarcard_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Generate Scholar Cards")
           
        popup_page.close()

        with page.expect_popup() as nweaschoollist_info:
            self.nweaschoollist= page.get_by_role("link", name=" Nwea School Lists")
            self.nweaschoollist.click()
            page.wait_for_timeout(12000)
            popup_page= nweaschoollist_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Nwea Schools")
            
        popup_page.close()

        self.viewscheduleplanglobal.click()
        page.wait_for_timeout(9000)
        self.valid1.validate_internal_roles(self.locators, "View Schedule Plans")
        

        self.nweatestresult.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "NWEA Test Result")
        


    def utilization_menu(self, page):
        self.utilization.click(timeout=0)
        page.wait_for_timeout(3000)

        with page.expect_popup() as teacherreport_info:
            self.teacherreport= page.get_by_role("link", name="Teacher Report")
            self.teacherreport.click()
            page.wait_for_timeout(24000)
            popup_page= teacherreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Teacher Utilization Report")
            
            
        popup_page.close()

        with page.expect_popup() as programreport_info:
            self.programreport= page.get_by_role("link", name="Program Report")
            self.programreport.click()
            page.wait_for_timeout(24000)
            popup_page= programreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Program Utilization Report")
            
        popup_page.close()


        with page.expect_popup() as schoolreport_info:
            self.schoolreport= page.get_by_role("link", name="School Report")
            self.schoolreport.click()
            page.wait_for_timeout(24000)
            popup_page= schoolreport_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "School Utilization Report")
           
        popup_page.close()

    def utilization_menuinternal(self, page):

        with page.expect_popup() as internal_info:
            self.internal= page.get_by_role("link", name="Internal")
            self.internal.click()
            page.wait_for_timeout(24000)
            popup_page= internal_info.value
            popup_page.wait_for_load_state("networkidle")
            locators= popup_page.locator('//*[@id="page-header"]/div/h2')
            self.valid1.validate_internal_roles(locators, "Internal Utilization Report")
            
        popup_page.close()


    def document_menu(self, page):
        self.document.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Document")
        

    def newfeature_menu(self, page):
        self.newfeature.click()
        page.wait_for_timeout(3000)
        self.viewstudentlist2.click(timeout=0)
        page.wait_for_timeout(13000)
        self.valid1.validate_internal_roles(self.locators, "Register Students")
        

    def classlink_menu(self, page):
        self.classlink.click(timeout=0)
        page.wait_for_timeout(3000)
        self.datasynclog.click(timeout=0)
        page.wait_for_timeout(9000)
        self.valid1.validate_internal_roles(self.locators, "Class Link Data Sync Log")
        
        self.continioussynclog.click(timeout=0)
        page.wait_for_timeout(4000)
        self.valid1.validate_internal_roles(self.locators, "Continuous Sync Log")
        

        self.newstudentaccounts.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "New Student Accounts")
        
        self.newuseraccounts.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "New User Accounts")
        

        self.newdistrictschool.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "New District/Schools")
        

        self.bulkschoolupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Class Link School Update")
        

        self.bulkstudentupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Class Link Student Update")
        

        self.bulkstudentupdateglobal.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Class Link Student Update")
        
        self.bulkuserupdate.click(timeout=0)
        page.wait_for_timeout(3000)
        self.valid1.validate_internal_roles(self.locators, "Bulk Class Link User Update")
        

        self.downloaddata.click(timeout=0)
        page.wait_for_timeout(12000)
        self.valid1.validate_internal_roles(self.locators, "Class Link Initial Data Sync")
        

        self.initiatedatasync.click(timeout=0)
        page.wait_for_timeout(12000)
        self.valid1.validate_internal_roles(self.locators, "Class Link Initial Data Sync")
        

        # with page.expect_popup() as classlinkroastersync_info:
        #     self.classlinkroaster= page.get_by_role("link", name="ClassLink Roaster Sync")
        #     self.classlinkroaster.click()
        #     page.wait_for_timeout(24000)
        #     popup_page= classlinkroastersync_info.value
        #     popup_page.wait_for_load_state("networkidle")
        #     try:
        #         expect(self.locators).to_have_text("")
        #         print("\nclasslink roaster page is working fine")

        #     except Exception as NameError:
        #         print("\n page is not found")
        # popup_page.close()


    def clever_menu(self, page):
        self.clever.click()
        page.wait_for_timeout(3000)
        self.datasynclog2.click(timeout=0)
        page.wait_for_timeout(4000)
        self.valid1.validate_internal_roles(self.locators, "Data Sync Log")
        

        self.continioussynclog2.click(timeout=0)
        page.wait_for_timeout(6000)
        self.valid1.validate_internal_roles(self.locators, "Continuous Sync Log")
        
        # self.newuseracccount2.click(timeout=0)
        # page.wait_for_timeout(80000)
        # try:
        #     expect(self.locators).to_have_text("New User Accounts")
        #     print("\n New user account clever page is working fine")

        # except Exception as NameError:
        #     print("\n New User Accounts clever page is not found")

        self.newuseraccountglobal2.click(timeout=0)
        page.wait_for_timeout(5000)
        self.valid1.validate_internal_roles(self.locators, "New User Accounts")
       
        self.newdistrictschool2.click(timeout=0)
        page.wait_for_timeout(5000)
        self.valid1.validate_internal_roles(self.locators, "New District/Schools")
       
        self.newdistrictschoolglobal2.click(timeout=0)
        page.wait_for_timeout(5000)
        self.valid1.validate_internal_roles(self.locators, "New District/Schools")
        
        self.initiatedatasync2.click(timeout=0)
        page.wait_for_timeout(12000)
        self.valid1.validate_internal_roles(self.locators, "Clever Initial Data Sync")
       

        # self.newstudentaccount2.click(timeout=0)
        # page.wait_for_timeout(80000)
        # try:
        #     expect(self.locators).to_have_text("New Student Accounts")
        #     print("\n New student accounts clever page is working fine")

        # except Exception as NameError:
        #     print("\n New Student Accounts clever page is not found")