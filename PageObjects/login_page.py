import openpyxl
from PageObjects import studenthome_page
from PageObjects.Adminhome_page import AdminHomepage
from PageObjects.cleverhome_page import Cleverhomepage
from PageObjects.devtomhome_page import devtomhomepage
from PageObjects.home_page import homepage
from PageObjects.studentgroupsession_page import studentgroupsession
from PageObjects.tutor_page import Tutorpage
from PageObjects.whiteboard_page import whiteboardpage
from Utilities.paths import get_excel_file_path
class LoginPage:

    def __init__(self,page):
       self.page = page
       
       self.wb = openpyxl.load_workbook(get_excel_file_path())
       self.portal_student_sheet = self.wb['Portal_Site_Student']
       self.portal_tutor_sheet = self.wb['Portal_Site_Tutor']

       self.admin_sheet = self.wb['Admin_Site_User']
       self.clever_sheet = self.wb['CleverUser']

       self.performance_stud_sheet = self.wb['Performance_Site_Student']
       self.performance_tutor_sheet = self.wb['Performance_Site_Tutor']

       self.staging_stud_sheet = self.wb['Staging_Site_Student']
       self.staging_tutor_sheet = self.wb['Staging_Site_Tutor']
       
       self.login_button= page.get_by_role("button", name="Login")
       self.submit_button = page.get_by_role("button", name="Submit")

    def username(self, username):
        self.page.fill("input[name='USER_NAME']", username)

    def password(self, password):
        self.page.fill("input[id='Password']", password)

    def loginbutton(self):
        self.login_button.click(timeout=0)

    def submitbutton(self):
        self.submit_button.click(timeout=0)
   
    def useremail(self, useremail):
        self.page.fill("input[name='email']", useremail)

#portal site student and tutor login for Ondeamnd Session

    def Ondemand_user_login(self):
        self.user_name= self.portal_student_sheet['A2'].value
        self.Password = str(self.portal_student_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def Ondemnd_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A2'].value
        self.Password = str(self.portal_tutor_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)
    
#performance site student and tutor login for Ondeamnd Session

    def performancesite_ondemand_userlogin(self):
        self.user_name= self.performance_stud_sheet['A2'].value
        self.Password = str(self.performance_stud_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def performancesite_ondemnd_tutor_login(self):
        self.user_name= self.performance_tutor_sheet['A6'].value
        self.Password = str(self.performance_tutor_sheet['B6'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#Staging site student and tutor login for Ondeamnd Session   
 
    def stagingsite_ondemand_userlogin(self):
        self.user_name= self.staging_stud_sheet['A2'].value
        self.Password = str(self.staging_stud_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def stagingsite_ondemnd_tutor_login(self):
        self.user_name= self.staging_tutor_sheet['A2'].value
        self.Password = str(self.staging_tutor_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#portal site student and tutor login for admin Session

    def Admin_user_login(self):
        self.user_name= self.portal_student_sheet['A3'].value
        self.Password = str(self.portal_student_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def Admin_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A3'].value
        self.Password = str(self.portal_tutor_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#performance site student and tutor login for admin Session

    def performancesite_admin_userlogin(self):
        self.user_name= self.performance_stud_sheet['A4'].value
        self.Password = str(self.performance_stud_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def performancesite_admin_tutor_login(self):
        self.user_name= self.performance_tutor_sheet['A2'].value
        self.Password = str(self.performance_tutor_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)


#Staging site student and tutor login for admin Session

    def stagingsite_admin_userlogin(self):
        self.user_name= self.staging_stud_sheet['A3'].value
        self.Password = str(self.staging_stud_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def stagingsite_admin_tutor_login(self):
        self.user_name= self.staging_tutor_sheet['A2'].value
        self.Password = str(self.staging_tutor_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#poratl site student and tutor login for Self Scheduele Session

    def Selfschedule_user_login(self):
        self.user_name= self.portal_student_sheet['A3'].value
        self.Password = str(self.portal_student_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def Selfschedule_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A3'].value
        self.Password = str(self.portal_tutor_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#perforamnce site student and tutor login for Self Scheduele Session

    def performancesite_selfschedule_userlogin(self):
        self.user_name= self.performance_stud_sheet['A10'].value
        self.Password = str(self.performance_stud_sheet['B10'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def performancesite_selfschedule_tutor_login(self):
        self.user_name= self.performance_tutor_sheet['A12'].value
        self.Password = str(self.performance_tutor_sheet['B12'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

#Staging site student and tutor login for Self Scheduele Session

    def stagingsite_selfschedule_userlogin(self):
        self.user_name= self.staging_stud_sheet['A16'].value
        self.Password = str(self.staging_stud_sheet['B16'].value)
        self.username(self.user_name)
        self.password(self.Password)
        self.loginbutton() 
        return homepage(self.page)
        
    def stagingsite_selfschedule_tutor_login(self):
        self.user_name= self.staging_tutor_sheet['A12'].value
        self.Password = str(self.staging_tutor_sheet['B12'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

# Admin site user devtom role login
    def user_devtom_login(self):
        self.user_name= self.admin_sheet['A2'].value
        self.Password = str(self.admin_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return devtomhomepage(self.page)

# Admin site user devscm role login   
    def user_devscm_login(self):
        self.user_name= self.admin_sheet['A5'].value
        self.Password = str(self.admin_sheet['B5'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()

# Admin site user devsm role login
    def user_devsm_login(self):
        self.user_name= self.admin_sheet['A6'].value
        self.Password = str(self.admin_sheet['B6'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()

# Admin site user devasc role login
    def user_devasc_login(self):
        self.user_name= self.admin_sheet['A7'].value
        self.Password = str(self.admin_sheet['B7'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()

# Admin site user deves role login
    def user_deves_login(self):
        self.user_name= self.admin_sheet['A8'].value
        self.Password = str(self.admin_sheet['B8'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()

# Admin site user devse role login
    def user_devse_login(self):
        self.user_name= self.admin_sheet['A3'].value
        self.Password = str(self.admin_sheet['B3'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return AdminHomepage(self.page)

# portal site student role login for session history
    def student_login(self):
        self.user_name= self.portal_student_sheet['A9'].value
        self.Password = str(self.portal_student_sheet['B9'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studenthome_page(self.page)
    
# Clever login
    def clever_login(self):
        self.user_email= self.clever_sheet['A2'].value
        self.Password = str(self.clever_sheet['B2'].value)
        self.useremail(self.user_email)
        self.password(self.Password) 
        self.submitbutton()
        return Cleverhomepage(self.page)

# portal group session creation login 
    def groupSession_Login_Page(self):
        self.user_name= self.admin_sheet['A5'].value
        self.Password = str(self.admin_sheet['B5'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
    
# Portal site First student login for group session 
    def studentgroupSessionone_Login_Page(self):
        self.user_name= self.portal_student_sheet['A4'].value
        self.Password = str(self.portal_student_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
# Portal site Second student login for group session 
    def studentgroupSessiontwo_Login_Page(self):
        self.user_name= self.portal_student_sheet['A5'].value
        self.Password = str(self.portal_student_sheet['B5'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
# Portal site Third student login for group session 
    def studentgroupSessionthree_Login_Page(self):
        self.user_name= self.portal_student_sheet['A6'].value
        self.Password = str(self.portal_student_sheet['B6'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)

# Portal site Tutor login for group session    
    def groupsessiontutor_login(self):
        self.user_name= self.portal_tutor_sheet['A4'].value
        self.Password = str(self.portal_tutor_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

    
# Performance site First student login for group session 
    def performancesite_studgpsessionone_Login_Page(self):
        self.user_name= self.performance_stud_sheet['A6'].value
        self.Password = str(self.performance_stud_sheet['B6'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
# Performance site Second student login for group session 
    def performancesite_studgpsessiontwo_Login_Page(self):
        self.user_name= self.performance_stud_sheet['A7'].value
        self.Password = str(self.performance_stud_sheet['B7'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
# Performance site Third student login for group session 
    def performancesite_studgpsessionthree_Login_Page(self):
        self.user_name= self.performance_stud_sheet['A8'].value
        self.Password = str(self.performance_stud_sheet['B8'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)

# Performance site Tutor login for group session    
    def performancesite_grpsessiontutor_login(self):
        self.user_name= self.performance_tutor_sheet['A8'].value
        self.Password = str(self.performance_tutor_sheet['B8'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

# Staging site First student login for group session 
    def stagingsite_studgpsessionone_Login_Page(self):
        self.user_name= self.staging_stud_sheet['A4'].value
        self.Password = str(self.staging_stud_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
#Staging site Second student login for group session 
    def stagingsite_studgpsessiontwo_Login_Page(self):
        self.user_name= self.staging_stud_sheet['A5'].value
        self.Password = str(self.staging_stud_sheet['B5'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
#Staging site Third student login for group session 
    def stagingsite_studgpsessionthree_Login_Page(self):
        self.user_name= self.staging_stud_sheet['A6'].value
        self.Password = str(self.staging_stud_sheet['B6'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)

# Staging site Tutor login for group session    
    def stagingsite_grpsessiontutor_login(self):
        self.user_name= self.staging_tutor_sheet['A2'].value
        self.Password = str(self.staging_tutor_sheet['B2'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)
    
    # portal group session creation login 
    def bulkondemand_Login_Page(self):
        self.user_name= self.admin_sheet['A5'].value
        self.Password = str(self.admin_sheet['B5'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()

   # Portal site bulk ondemand student login
    def bulk_ondemand_student_login(self):
        self.user_name= self.portal_student_sheet['A13'].value
        self.Password = str(self.portal_student_sheet['B13'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
    # Portal site bulk ondemand Tutor login 
    def bulk_ondemand_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A4'].value
        self.Password = str(self.portal_tutor_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)
    
    # Portal site bulk ondemand student login
    def tsa_student_login(self):
        self.user_name= self.portal_student_sheet['A7'].value
        self.Password = str(self.portal_student_sheet['B7'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
    def tsa_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A10'].value
        self.Password = str(self.portal_tutor_sheet['B10'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)
    
    def tsa_tutortwo_login(self):
        self.user_name= self.portal_tutor_sheet['A11'].value
        self.Password = str(self.portal_tutor_sheet['B11'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)
    
    def tsa_tutorthree_login(self):
        self.user_name= self.portal_tutor_sheet['A12'].value
        self.Password = str(self.portal_tutor_sheet['B12'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

    # Portal site bulk session student login
    def bulk_session_student_login(self):
        self.user_name= self.portal_student_sheet['A13'].value
        self.Password = str(self.portal_student_sheet['B13'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return studentgroupsession(self.page)
    
    # Portal site bulk session Tutor login   
    def bulk_session_tutor_login(self):
        self.user_name= self.portal_tutor_sheet['A4'].value
        self.Password = str(self.portal_tutor_sheet['B4'].value)
        self.username(self.user_name)
        self.password(self.Password) 
        self.loginbutton()
        return Tutorpage(self.page)

    # Portal site bulk session with pgm student login
    def bulk_session_with_pgm_student_login(self):
        self.user_name= self.portal_student_sheet['A17'].value
        self.Password = str(self.portal_student_sheet['B17'].value)
        self.username(self.user_name)
        self.password(self.Password)       
        self.loginbutton()
        return homepage(self.page)
    