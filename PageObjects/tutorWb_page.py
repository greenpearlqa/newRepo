from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import download_Tutor_WB_Screenshot

class TutorWB:
    def __init__(self,page):
        # Initialize the homepage class with a Playwright page object
        try:
            self.page = page
        # Create an assertionandvalidation instance
            self.assert_validate = assertionandvalidation()

            with page.expect_popup() as wbpage_info:
                self.page.wait_for_timeout(3000)
                self.ondemandjoinnow = page.get_by_role("button", name="Join Now")
                self.joinnow = page.locator("#popupBtnJoinNow").get_by_role("button", name="Join Now")
                # self.adminjoinnow = page.locator('//input[@id="btnJoinNow"]')
            wbpage = wbpage_info.value
        # Elements on the page
            self.highlighter = wbpage.locator('#btnHighlighter')
            self.chatbox = wbpage.get_by_placeholder("Type your message here..")
            self.message = wbpage.get_by_placeholder("Type your message here..")
            self.send_msg = wbpage.get_by_placeholder("Type your message here..")
            self.wbmouse = wbpage
            self.pencil = wbpage.locator('#btnPencil')
            self.Pointer = wbpage.locator('#btnPointer')
            self.Addtext = wbpage.locator('#btnAddText')
            self.Addingtext = wbpage.locator('#txtadd')
            self.Grid = wbpage.locator('#btnGrid')
            self.media = wbpage.get_by_role("button", name="Open Media")
            self.mediafill = wbpage.get_by_placeholder("URL")
            self.play = wbpage.get_by_role("button", name="Play")
            self.mediaclose = wbpage.get_by_role("link", name="Close")
            self.fileupload = wbpage.get_by_role("button", name="File Upload")
            self.fileuploadwb = wbpage.locator("#fileToUpload")
            self.fileuploadinput = wbpage.locator("#fileToUpload")
            self.fileuploadbutton = wbpage.get_by_role("button", name="File Upload")
            self.fileclose = wbpage.get_by_role("button", name="close")
            self.selectlanguage = wbpage.get_by_role("link", name="Select Language")
            self.languagechange = wbpage.frame_locator("iframe[title=\"Language Translate Widget\"]").get_by_role("link", name="›English")
            self.languageclose = wbpage.locator('//*[@id=":2.close"]/img')
            self.library_button = wbpage.get_by_role("button", name="Library")
            #PPT
            self.ppt_upload = wbpage.get_by_text("FEVTutor On-Demand Welcome Slides.ppt")
            #math content
            self.content_upload = wbpage.get_by_role("button", name="Content")
            self.math_content = wbpage.get_by_role("button", name="1.2.ACT.2.Distance Formula")
            self.math_content_nextpage = wbpage.locator("(//span[@class='olt_sarrow olt_snext'])[1]")
            self.math_lesson = wbpage.locator("li").filter(has_text="258852")
            #self.math_next_page = wbpage.locator("#N-OLT-5419-1108143633375-0")
            # self.math_view_question = wbpage.get_by_role("button", name="View Question")
            # self.math_close_question = wbpage.get_by_role("img", name="Close")
            # self.view_math_notes = wbpage.get_by_role("button", name="View Notes")
            # self.math_notes_close = wbpage.get_by_role("img", name="Close")
            
            #Ela content
            self.ela_upload = wbpage.locator("#rd_olt_ela")
            self.ela_content = wbpage.get_by_role("button", name="1.1.RI.1.Asking and Answering Questions")
            self.ela_content_nextpage = wbpage.locator('(//span[@class="olt_sarrow olt_snext"])[2]')
            self.Gp_ela_nextpage = wbpage.locator('//span[@class="olt_sarrow olt_snext"]')
            self.view_note_button = wbpage.get_by_role("button", name="View Notes")
            self.view_text = wbpage.get_by_text("Using question words such as What, Where, When, Who, Why, and How will help you ")
            self.play_stop_button = wbpage.get_by_role("button", name="Play/Stop")
            self.viewnote_close_button = wbpage.get_by_role("img", name="Close")
            self.passage_button = wbpage.get_by_role("button", name="View Passage")
            self.passage_text = wbpage.locator("#d_ela_pop_tabs-1112917523298_3_s").get_by_text("Read the story below.")
            self.passageClose_button= wbpage.locator("xpath=//img[@class='olt_pop_close']")
            #Science content    
            self.science_upload = wbpage.locator("#rd_olt_science")
            self.science_content = wbpage.get_by_role("button", name="3.8B.1.1.Character Traits")
            self.science_content_nextpage = wbpage.locator('(//span[@class="olt_sarrow olt_snext"])[3]')
            #self.science_nextpage = wbpage.locator("#N-OLT-6162-11013489973430-0")
            # self.view_science_notes = wbpage.get_by_role("button", name="View Notes")
            # self.close_science_notes = wbpage.get_by_role("img", name="Close")

            #Social/History Content
            self.social_content_upload = wbpage.locator("#rd_olt_sscience")
            self.select_social_lesson = wbpage.get_by_role("button", name="11 - 12.GA.2.2.Big Business & Political Corruption")
            self.social_next_page = wbpage.locator("(//span[@class='olt_sarrow olt_snext'])[4]")
            self.social_notes = wbpage.get_by_role("button", name="S", exact=True)
            self.social_notes_show = wbpage.get_by_role("button", name="Show")
            self.social_img = wbpage.get_by_role("button", name="I", exact=True)
            self.social_img_view = wbpage.get_by_role("button", name="Show")
            #end session
            self.endsession = wbpage.get_by_role("button", name="END SESSION")
            self.student_two = wbpage.locator('//a[@id="1971138"]')
            self.student_three = wbpage.locator('//a[@id="1971139"]')
            self.endsessionok = wbpage.get_by_role("button", name="OK")
            self.grp_back = wbpage.get_by_role("button", name="Back")

            self.manualcheck = wbpage.locator("#chkManual")
            self.participation = wbpage.get_by_role("textbox", name="Participation points...")
            self.participationpoints = wbpage.get_by_role("textbox", name="Participation points...")
            self.exitticket = wbpage.get_by_role("textbox", name="Please enter no. of exit ticket questions attempted.")
            self.exitticketfill = wbpage.get_by_role("textbox", name="Please enter no. of exit ticket questions attempted.")
            self.exitticketearned = wbpage.get_by_role("textbox", name="Please enter exit ticket points earned.")
            self.exitticketearnedfill = wbpage.get_by_role("textbox", name="Please enter exit ticket points earned.")
            self.progressnotes = wbpage.locator("#txtProgressNotes")
            self.progressnotesfill = wbpage.locator("#txtProgressNotes")
            self.progressnotestab = wbpage.locator("#txtProgressNotes")
            self.tutorcomments = wbpage.locator("#txtTutorComments")
            self.submit = wbpage.get_by_role("button", name="Submit")
            self.feedback_backbutton = wbpage.locator('//button[@id="RefreshPage"]')
            self.feedbackpageclose = wbpage
            self.timer_button = wbpage.get_by_role("button", name="Timers")
            #self.poll = wbpage.get_by_role("button", name="Poll")
            self.poll = wbpage.locator('//input[@id="btnPolling"]')
            self.createpoll = wbpage.get_by_role("button", name="Create a Poll")
            self.poll_question = wbpage.locator("#txtpollquestion")
            self.first_option_ans = wbpage.locator("#divpolloptions textarea").first
            self.second_option_ans = wbpage.locator("#divpolloptions textarea").nth(1)
            self.third_option_ans = wbpage.locator("#divpolloptions textarea").nth(2)
            self.move_button = wbpage.get_by_role("button", name="Move")
            self.pollquestion = wbpage.locator("#txtpollquestion_1")
            self.pollquestionfill = wbpage.locator("#txtpollquestion_1")
            self.firstoption = wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(1)
            self.firstoptionfill =wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(1)
            self.secondoption = wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(2)
            self.secondoptionfill = wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(2)
            self.thirdoption = wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(3)
            self.thirdoptionfill = wbpage.get_by_role("dialog", name="Poll").locator("textarea").nth(3)
            self.saveandpublish = wbpage.get_by_role("button", name="Save and Publish")
            self.endpoll = wbpage.get_by_role("button", name="End Poll")
            self.poll_close = wbpage.get_by_role("button", name="close")
            self.ela_ok_button = wbpage.get_by_role("button", name="OK")
            self.screen_share_button = page.get_by_role("button", name="Screen-Share")
            self.screen_share_ok_button = page.get_by_role("button", name="OK")
            
            self.end_poll_tutor = wbpage.locator('//input[@id="btnpollend"]')
            
            self.poll_close_tutor = wbpage.locator('(//span[@class="ui-icon ui-icon-closethick"])[1]')
            self.Goslow_ok_button = wbpage.locator('//input[@id="b_statusok"]')
            #language
            self.language_ok_button= wbpage.locator('//*[@id="alertify-ok"]')

            self.session_id_element = wbpage.locator('label:has-text("Session ID :") + input[name="SessionID"]')
            # SGT
            self.Move_button = wbpage.get_by_role("button", name="Move")
            self.sgtstud_one = wbpage.locator("#sel_usr_room_2")
            self.sgtstud_two = wbpage.locator("#sel_usr_room_3")
            self.sgtstud_three = wbpage.locator("#sel_usr_room_4")
            self.move_ok_button = wbpage.locator('//input[@id="btn_br_move_ok"]')
            self.control_pannel = wbpage.get_by_role("button", name="Control Panel")

            # Extend Min
            self.extendmin_button = wbpage.get_by_role("button", name="EXTEND MINS")   
            self.select_extendmin = wbpage.locator("#selExtMins")
            self.alert_before = wbpage.locator("#selExtAlert")
            self.extendmin_ok_button = wbpage.locator('//input[@id="btnOkExt"]')
            self.suresetting= wbpage.locator('//button[@id="alertify-ok"]')

            # Timer
            self.timer = wbpage.get_by_role("button", name="Countdown timer")
            self.timer_min = wbpage.get_by_placeholder("Min")
            self.timer_sec= wbpage.get_by_placeholder("Sec")
            self.start = wbpage.get_by_role("button", name="Start")
            self.timer_close = wbpage.locator('(//img[@alt="Close"])[1]')

            #Colour
            self.colour= wbpage.locator("#DColorPick")
            self.red_colour = wbpage.locator("#colorPicker_palette-1 > div:nth-child(2)")
            self.black_colour = wbpage.locator(".colorPicker-swatch").first

            # Scrrenshot
            self.Screenshot_button = wbpage.get_by_role("button", name="Screenshot")
            #self.download_ss = wbpage.get_by_text("Click here to download")
            self.SS = wbpage.get_by_role("img", name="Screenshot")
            #self.SS_close_button = wbpage.locator('(//img[@alt="Close"])[3]')
            self.SS_close_button = wbpage.locator('(//img[@src="../../Images/ico_pop_close.png"])[1]')
            

            # Teacher Alert
            self.teacher_alert = wbpage.get_by_role("button", name="Teacher Alert")
            self.select_student_option = wbpage.get_by_role("button", name="Student is off Topic")

        
        except:
            print("exception")

    def tutorwb_chatbox(self):
    # Click on "chatbox " and enter some massage  
        if self.assert_validate.validate_attributes(self,'chatbox', 'tutorWB_page'):
            return
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Hello QA Team")
        self.send_msg.press("Enter")
    
    def tutorwb_highlighter(self):
    # Click on " highlighter "
        if self.assert_validate.validate_attributes(self,'highlighter', 'tutorWB_page'):
            return
        #self.wbmouse.bring_to_front()
        self.page.wait_for_timeout(1000)
        self.highlighter.click()
        self.wbmouse.mouse.move(100, 100)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(200, 200)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I am using Highlighter")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(1000)
    
    def tutorwb_pencil(self):
    # Click on "Pencil"
        if self.assert_validate.validate_attributes( self,'pencil', 'tutorWB_page'):                    
            return
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I am using pencil")
        self.send_msg.press("Enter")
        self.pencil.click(timeout=0)
        self.wbmouse.mouse.move(350, 250)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(230, 230)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(2000)
    
    def tutorwb_pointer(self):
    # Click on "Pointer"
        if self.assert_validate.validate_attributes( self,'Pointer', 'tutorWB_page'):                    
            return  
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I am using Pointer")
        self.send_msg.press("Enter")
        self.Pointer.click(timeout=0)
        self.wbmouse.mouse.move(100, 100)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(100, 100)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(2000)
    
    def tutorwb_AddText(self):
    # Click on "Add Text"
        if self.assert_validate.validate_attributes( self,'Addtext', 'tutorWB_page'):                    
            return   
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I am using Text")
        self.send_msg.press("Enter")
        self.Addtext.click(timeout=0)
        self.wbmouse.mouse.move(300, 200)
        self.wbmouse.mouse.click(300, 200)
        self.Addingtext.fill("Testing")
        self.wbmouse.mouse.click(800, 500)
        self.page.wait_for_timeout(1000) 
                
    def tutorwb_grid(self):
    # Click on "Grid"
        if self.assert_validate.validate_attributes(self,'Grid', 'tutorWB_page'):
            return 
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I am using Grid")
        self.send_msg.press("Enter")
        self.Grid.click(timeout=0)
        self.wbmouse.mouse.move(600, 350)
        self.wbmouse.mouse.down()      
        self.wbmouse.mouse.move(400, 320)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(1000)
        
    def tutorwb_media_chat(self):
    # Click on "Media"
        if self.assert_validate.validate_attributes( self,'media', 'mediafill','play','tutorWB_page'):                    
            return
        self.media.click(timeout=0)
        self.mediafill.fill("https://www.youtube.com/watch?v=-Do8F1PeUXg")
        self.play.click()
        self.page.wait_for_timeout(1000)       
        self.chatbox.click(timeout=0)
        self.message.fill("Media Playing")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(5000)
        self.mediaclose.click()
           
    def tutorwb_image_ppt_content(self):
    # click on "Library " and Upload "PPT"
        if self.assert_validate.validate_attributes(self,'library_button', 'ppt_upload','tutorWB_page'):                    
            return
        self.library_button.click(timeout=0)
        self.page.wait_for_timeout(5000)
    # After selecting Student Upload the PPT OR CONTENT 
        self.ppt_upload.click(timeout=0)
        self.page.wait_for_timeout(10000)
        self.wbmouse.mouse.move(100, 100)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(200, 200)
        self.wbmouse.mouse.up()
    # Enter some message
        self.chatbox.click(timeout=0)
        self.chatbox.fill("PPT loaded")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(1000)
    
    def Math_content_upload(self):
    # click on "Library" and Upload "Math" content
        if self.assert_validate.validate_attributes(self,'library_button', 'content_upload','tutorWB_page'):                    
            return
        self.library_button.click(timeout=0)
        self.content_upload.click(timeout=0)
        self.math_content.click(timeout=0)
        self.math_content_nextpage.click(timeout=0)
        self.math_lesson.click(timeout=0)
        self.page.wait_for_timeout(5000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Math Loaded")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)

    def Ela_Content_upload(self):
    # click on "Library" and Upload "English" content
        if self.assert_validate.validate_attributes(self,'library_button', 'ela_upload','ela_content','ela_content_nextpage','tutorWB_page'):                    
            return
        self.library_button.click(timeout=0)
        self.ela_upload.check(timeout=0)
        self.ela_content.click(timeout=0)
        self.ela_content_nextpage.click(timeout=0)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("ELA Loaded")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(5000)
      
    def Science_content_upload(self):
    # click on "Library" and Upload "Sciecne" content
        if self.assert_validate.validate_attributes(self,'library_button', 'science_upload','science_content','science_content_nextpage','tutorWB_page'):                    
            return
        self.library_button.click(timeout=0)
        self.science_upload.check(timeout=0)
        self.science_content.click(timeout=0)
        self.science_content_nextpage.click(timeout=0)
        self.page.wait_for_timeout(5000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Science loaded")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(3000)

    def Social_content_upload(self):
    # click on "Library" and Upload "Social/History" content
        if self.assert_validate.validate_attributes(self,'library_button', 'social_content_upload','select_social_lesson','social_next_page','tutorWB_page'):                    
            return
        self.library_button.click(timeout=0)
        self.social_content_upload.check()
        self.select_social_lesson.click(timeout=0)
        self.social_next_page.click()
        self.social_notes.click()
        self.social_notes_show.click()
        self.social_img.click()
        self.social_img_view.click()
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Social loaded")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)
        
    def tutorwb_groupsession_image_ppt_content(self):
    # click on "Library" and Upload "PPT and ELA " content
        if self.assert_validate.validate_attributes(self,'library_button', 'ppt_upload','content_upload','ela_upload','ela_content','Gp_ela_nextpage','tutorWB_page'):                    
            return
        self.wbmouse.bring_to_front()
        self.library_button.click(timeout=0)
        self.page.wait_for_timeout(5000)       
        # upload PPT
        self.ppt_upload.click(timeout=0)
        self.page.wait_for_timeout(3000)
        #performd basic tools on PPT
        self.wbmouse.mouse.move(100, 100)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(200, 200)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(3000)
        # then upload ELA
        # this code for student's in common tab then upload ELA
        self.library_button.click(timeout=0)
        self.content_upload.click(timeout=0)
        self.ela_upload.check(timeout=0)                     
        self.ela_content.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.Gp_ela_nextpage.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.view_note_button.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.viewnote_close_button.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.passage_button.click(timeout=0)
        self.passageClose_button.click(timeout=0)
        self.page.wait_for_timeout(2000)
    
    def tutorwb_polls(self):
    # click on "Poll" and create a Poll
        if self.assert_validate.validate_attributes(self,'ela_ok_button', 'poll','createpoll','tutorWB_page'):                    
            return
        #self.wbmouse.bring_to_front()
        #self.ela_ok_button.click(timeout=0)
        self.poll.click()
        self.createpoll.click()
        self.pollquestion.click()
        self.pollquestionfill.fill("browser?")
        self.firstoption.first.click()
        self.firstoptionfill.first.fill("chrome")
        self.secondoption.click()
        self.secondoptionfill.fill("firefox")
        # self.thirdoption.click()
        # self.thirdoptionfill.fill("Edge")
        self.saveandpublish.click()
        self.page.wait_for_timeout(2000)

    def tutorwb_group_polls(self):
    # click on "Poll" and create a Poll
        if self.assert_validate.validate_attributes(self,'ela_ok_button', 'poll','createpoll','tutorWB_page'):                    
            return
        #self.wbmouse.bring_to_front()
        #self.ela_ok_button.click(timeout=0)
        self.poll.click()
        self.createpoll.click()
        self.pollquestion.click()
        self.pollquestionfill.fill("browser?")
        self.firstoption.first.click()
        self.firstoptionfill.first.fill("chrome")
        self.secondoption.click()
        self.secondoptionfill.fill("firefox")
        #self.thirdoption.click()
        #self.thirdoptionfill.fill("Edge")
        self.saveandpublish.click()
    
    def tutorwb_end_polls(self):
    # End the Poll after student submitting the poll answer 
        if self.assert_validate.validate_attributes(self,'endpoll', 'poll_close','tutorWB_page'):                    
            return
        # self.wbmouse.bring_to_front()
        #self.ela_ok_button.click(timeout=0)
        # self.wbmouse.bring_to_front()
        #self.end_poll_tutor.wait_for_selector_state("visible")
        #self.end_poll_tutor.wait_for_selector_state("enabled")
        self.end_poll_tutor.click()
        self.poll_close_tutor.click()
    
    def tutorwb_language(self):
    # Change "language"
        if self.assert_validate.validate_attributes(self,'language_ok_button','tutorWB_page'):                    
            return
        self.language_ok_button.click(timeout=0)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("ok")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(1000)
        
    def session_end_feedback(self):
    # click on "End Session " and submit the feedback 
        if self.assert_validate.validate_attributes(self,'manualcheck', 'participation','tutorWB_page'):                    
            return
        self.manualcheck.check()
        self.participation.dblclick()
        self.participationpoints.fill("7")
        self.exitticket.click()
        self.exitticketfill.fill("6")
        self.exitticketearned.click()
        self.exitticketearnedfill.fill("3")
        self.progressnotes.click()
        self.progressnotesfill.fill("Testing")
        self.progressnotestab.press("Tab")
        self.tutorcomments.fill("Test")
        self.submit.click()
        #self.feedback_backbutton.click()

    def tutorwb_close(self):
        self.wbmouse.close()
    
    def tutor_endsession_feedback(self):
    # click on "End Session " and submit the feedback 
        if self.assert_validate.validate_attributes(self,'endsession', 'endsessionok','tutorWB_page'):                    
            return
        self.page.wait_for_timeout(1000)
        self.chatbox.click()
        self.chatbox.fill("Yes language change")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(1000)
        self.endsession.click()
        self.endsessionok.click()
        self.page.wait_for_timeout(1000)
        # self.session_end_feedback()

    def tutor_end_groupsession_feedback(self):
    # click on "End Session " and submit the feedback 
        if self.assert_validate.validate_attributes(self,'endsession', 'endsessionok','tutorWB_page'):                    
            return  
        self.wbmouse.bring_to_front()
        self.endsession.click()
        self.endsessionok.click()
        self.page.wait_for_timeout(1000)
        # self.session_id()
        self.session_end_feedback()
        self.grp_back.click()
        # second Student feedback page from tutor side
        self.page.wait_for_timeout(1000)
        self.student_two.click()
        self.session_end_feedback()
        #Third Student Feedback Page  
        self.grp_back.click()
        self.page.wait_for_timeout(1000)  
        self.student_three.click()
        self.session_end_feedback()
    
    def session_id(self):
        session_id_value = self.session_id_element.get_attribute('value')
        print(f"Session ID: {session_id_value}")

    def tutorWb_SGT_groupsession(self):
        self.Move_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.sgtstud_one.select_option("tabs-2")
        self.page.wait_for_timeout(1000)
        self.sgtstud_two.select_option("tabs-3")
        self.page.wait_for_timeout(1000)
        self.sgtstud_three.select_option("tabs-4")
        self.page.wait_for_timeout(1000)
        self.move_ok_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.control_pannel.click(timeout=0)


    def tutorWb_slowDown(self):
        if self.assert_validate.validate_attributes(self,'Goslow_ok_button','tutorWB_page'):                    
            return  
        self.page.wait_for_timeout(1000)
        self.Goslow_ok_button.click(timeout=0)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Yes i got a goslow button popup")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(1000)

    def tutorWb_extendMinDuration(self):
        if self.assert_validate.validate_attributes(self,'extendmin_button','select_extendmin', 'alert_before','tutorWB_page'):                    
            return
        self.page.wait_for_timeout(1000)
        self.extendmin_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.select_extendmin.select_option("10")
        self.page.wait_for_timeout(1000)
        self.alert_before.select_option("5")
        self.page.wait_for_timeout(1000)
        self.extendmin_ok_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.suresetting.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("I have extend extra 10 min")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)


    def tutorWb_Countdown_timer(self):
        if self.assert_validate.validate_attributes(self,'timer','timer_min', 'timer_sec','tutorWB_page'):                    
            return
        self.timer.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.timer_min.click(timeout=0)
        self.timer_min.fill("10")
        self.page.wait_for_timeout(1000)
        self.timer_sec.click(timeout=0)
        self.timer_sec.fill("05")
        self.page.wait_for_timeout(1000)
        self.start.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.timer_close.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Countdown Timer started")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)

    def tutorWb_color_picker_selection(self):
        if self.assert_validate.validate_attributes(self,'colour','red_colour', 'black_colour','tutorWB_page'):                    
            return
        
        self.colour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.red_colour.click(timeout=0)
        self.page.wait_for_timeout(3000)
        self.highlighter.click()
        self.wbmouse.mouse.move(500, 100)
        self.wbmouse.mouse.down()
        self.wbmouse.mouse.move(800, 200)
        self.wbmouse.mouse.up()
        self.page.wait_for_timeout(1000)
        self.colour.click(timeout=0)
        self.black_colour.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Colour Picker working")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)

    def tutorWB_capture_screenshot(self):
        if self.assert_validate.validate_attributes(self,'Screenshot_button','SS_close_button', 'chatbox','tutorWB_page'):                    
            return
        self.Screenshot_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.SS.click(timeout=0)
        self.page.wait_for_timeout(1000)
        '''
        
        with self.page.expect_download() as download_info:
            self.page.locator('//div[@class="Click-here-to-download"]').click(timeout=0)
            self.page.wait_for_timeout(1000)
        download = download_info.value
        #download.save_as(download_Tutor_WB_Screenshot())
        #self.page.wait_for_timeout(1000)
        
        '''
       
        self.SS_close_button.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Screenshot working")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)

    def tutorWb_teacher_alert_handler(self):
        if self.assert_validate.validate_attributes(self,'teacher_alert','select_student_option', 'tutorWB_page'):                    
            return   
        self.teacher_alert.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.select_student_option.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.chatbox.click(timeout=0)
        self.chatbox.fill("Teacher Alert Sent")
        self.send_msg.press("Enter")
        self.page.wait_for_timeout(2000)





