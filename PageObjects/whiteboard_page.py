import time
from Utilities.assertion_validation import assertionandvalidation
from Utilities.paths import get_image_file_path, get_pdf_file_path

class whiteboardpage:
      
      def __init__(self,page):
      # Initialize the homepage class with a Playwright page object
            self.page = page
      # Create an assertionandvalidation instance
            self.assert_validate = assertionandvalidation()
      # Elements on the page
            self.chatbox = page.get_by_placeholder("Type your message here..")
            self.message = page.get_by_placeholder("Type your message here..")
            self.send_msg = page.get_by_placeholder("Type your message here..")
            self.highlighter = page.locator('#btnHighlighter')
            self.wbmouse = page
            self.pencil = page.locator('#btnPencil')
            self.Pointer = page.locator('#btnPointer')
            self.Addtext = page.locator('#btnAddText')
            self.Addingtext = page.locator('#txtadd')
            self.Grid = page.locator('#btnGrid')
            self.media = page.get_by_role("button", name="Open Media")
            self.mediafill = page.get_by_placeholder("URL")
            self.play = page.get_by_role("button", name="Play")
            self.mediaclose = page.get_by_role("link", name="Close")
            self.fileupload = page.get_by_role("button", name="File Upload")
            self.fileuploadwb = page.locator("#fileToUpload")
            self.fileuploadinput = page.locator("#fileToUpload")
            self.fileuploadbutton = page.get_by_role("button", name="File Upload")
            self.fileclose = page.get_by_role("button", name="close")
            self.pollanswer = page.get_by_role("row", name="chrome").get_by_role("cell")
            #self.pollsubmit = page.get_by_role("button", name="Submit")
            self.pollsubmit = page.locator('xpath=//input[@id="btnAttSubmit"]')
            self.gp_pollclose = page.get_by_role("button", name="Close", exact=True)
            self.poll_close = page.locator('xpath=//input[@id="btnpcl"]')
            self.pollclose = page.locator('//input[@id="btnpcl"]')
            #language 
            self.selectlanguage = page.get_by_role("link", name="Select Language​")
            self.spanish_language = page.frame_locator("iframe[title=\"Language Translate Widget\"]").get_by_role("link", name="›Spanish")
            self.sendchat = page.get_by_placeholder("Escribe tu mensaje aquí..")
            self.send_button = page.locator("#btnSend")
            self.orignal_lang = page.frame_locator('//span[@id=":2.promptTargetLang"]')
            self.french_language = page.frame_locator("iframe[title=\"Language Translate Widget\"] >> nth=0").get_by_role("link", name="›French")
            self.fench_chat = page.get_by_placeholder("Tapez votre message ici..")
            self.iframe = page.locator('//iframe[@id=":2.container"]')
            self.ela_answer= page.get_by_placeholder("Type your Answer here..")
            self.ela_ans_submit_button = page.get_by_role("button", name="Submit")
            self.GoSlow_button = page.get_by_role("button", name="Go Faster")
            self.eraser_button = page.get_by_role("button", name="Eraser")
            self.smiley_button = page.get_by_role("button", name="Smiley Icons")
            self.smiley_one = page.locator("#v2-Smiley_6")
            self.smiley_two = page.locator("#v2-Smiley_3")
            self.colour = page.locator("#DColorPick")
            self.red_colour = page.locator("#colorPicker_palette-1 > div:nth-child(2)")
            self.zoom_min = page.get_by_role("button", name="Zoom In")
            self.reset_zoom = page.get_by_role("button", name="Reset Zoom")
            self.zoom_out= page.get_by_role("button", name="Zoom Out")
            self.undo_button = page.get_by_role("button", name="Undo")
            self.redo_button = page.get_by_role("button", name="Redo")
            self.shapes= page.get_by_role("button", name="Shapes", exact=True)
            self.rectangle = page.get_by_role("button", name="Rectangle")
            self.pentagon = page.get_by_role("button", name="Pentagon")
            self.heptagon = page.get_by_role("button", name="Heptagon")
            self.otagon = page.get_by_role("button", name="Octagon")
            self.line = page.get_by_role("button", name="Line")
            self.circle = page.get_by_role("button", name="Circle/Ellipse")

            self.delete = page.get_by_role("button", name="Delete")





       
      def student_chat(self):
      # click on "chatbox" and enter some message
            if self.assert_validate.validate_attributes(self,'chatbox', 'whiteboard_page'):
                  return
            self.chatbox.click()
            self.chatbox.fill("Hello Tutor")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(3000)

      def WB_highlighter(self):
      # Click on "Highlighter" 
            if self.assert_validate.validate_attributes(self,'highlighter', 'whiteboard_page'):
                  return
            self.highlighter.click(timeout=0)
            self.wbmouse.mouse.move(100, 100)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(200, 200)
            self.wbmouse.mouse.up()
            self.chatbox.click()
            self.chatbox.fill("I am using highlighter")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(5000)
                        
      def WB_pencil(self):
      # Click on "Pencil"
            if self.assert_validate.validate_attributes(self,'pencil', 'whiteboard_page'):
                  return
            self.pencil.click(timeout=0)
            self.wbmouse.mouse.move(350, 250)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(230, 230)
            self.wbmouse.mouse.up()
            self.chatbox.click()
            self.chatbox.fill("I am using pencil ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(5000)

      def WB_pointer(self):
      # Click on "Pointer"
            if self.assert_validate.validate_attributes(self,'Pointer', 'whiteboard_page'):
                  return
            self.Pointer.click(timeout=0)
            self.wbmouse.mouse.up()
            self.wbmouse.mouse.move(100, 100)
            self.page.wait_for_timeout(10000)
            self.chatbox.click()
            self.chatbox.fill("I am using Pointer ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(10000)
                          
      def WB_addText(self):
      # Click on "Add text"
            if self.assert_validate.validate_attributes(self,'Addtext','Addingtext', 'whiteboard_page'):
                  return
            self.Addtext.click(timeout=0)
            self.wbmouse.mouse.move(300, 200)
            self.wbmouse.mouse.click(300, 200)
            self.page.wait_for_timeout(1000)
            self.Addingtext.fill("Testing")
            self.wbmouse.mouse.click(800, 500)
            self.wbmouse.mouse.up()
            self.chatbox.click()
            self.chatbox.fill(" Text Audible ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)

      def WB_grid(self):
      # click on "Grid"
            if self.assert_validate.validate_attributes(self,'Grid','whiteboard_page'):
                  return
            self.Grid.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.chatbox.click()
            self.chatbox.fill(" Grid working ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(10000)
            
      def Wb_media_chat(self):
      # click on "Media" 
            if self.assert_validate.validate_attributes(self,'media','mediafill','play','mediaclose', 'whiteboard_page'):
                  return
            self.media.click(timeout=0)
            self.mediafill.fill("https://www.youtube.com/watch?v=-Do8F1PeUXg")
            self.play.click(timeout=0)
            self.page.wait_for_timeout(10000)
            self.chatbox.click(timeout=0)
            self.message.fill("Media Playing")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(15000)
            self.mediaclose.click()

      def student_poll(self):
      # Submit the Poll answer
            if self.assert_validate.validate_attributes(self,'pollanswer', 'pollsubmit', 'poll_close', 'pollclose','whiteboard_page'):
                  return
            self.page.wait_for_timeout(1000)
            self.pollanswer.first.click(timeout=0)
            self.page.wait_for_timeout(100)
            self.pollsubmit.click()
            #self.gp_pollclose.click()
            # self.poll_close.click()
            self.page.wait_for_timeout(1000)
            self.pollclose.click(timeout=0)
            self.chatbox.click()
            self.chatbox.fill("Yes Poll submitted")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)

      def student_group_poll(self):
      # Submit the Poll answer
            if self.assert_validate.validate_attributes(self,'pollanswer', 'pollsubmit', 'gp_pollclose', 'poll_close','whiteboard_page'):
                  return 
            self.page.wait_for_timeout(1000)
            self.pollanswer.first.click(timeout=0)
            self.page.wait_for_timeout(100)
            self.pollsubmit.click()
            self.gp_pollclose.click()
            # self.poll_close.click()
            self.page.wait_for_timeout(1000)
            self.chatbox.click()
            self.chatbox.fill("Yes Poll submitted")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)

      def student_library_chatbox(self):
      # Student Enter the Library details in chatbox
            if self.assert_validate.validate_attributes(self,'chatbox', 'send_msg', 'whiteboard_page'):
                 return
            self.chatbox.click()
            self.chatbox.fill(" PPT Loaded")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            # self.chatbox.click()
            # self.chatbox.fill("Yes ELA Loaded")
            # self.send_msg.press("Enter")
            # self.page.wait_for_timeout(3000)
            # self.chatbox.click()
            # self.chatbox.fill("Yes Science Loaded")
            # self.send_msg.press("Enter")
            # self.page.wait_for_timeout(3000)
            # self.chatbox.click()
            # self.chatbox.fill("Yes Social/History Loaded")
            # self.send_msg.press("Enter")
            # self.page.wait_for_timeout(3000)
      
      def ela_answers(self):
      # Click on ELA and submit the answer
            if self.assert_validate.validate_attributes(self,'wbmouse', 'ela_answer', 'ela_ans_submit_button', 'whiteboard_page'):
                 return
            self.wbmouse.bring_to_front()
            self.ela_answer.click(timeout=0)
            self.ela_answer.fill("Hello Team")
            self.ela_ans_submit_button.click(timeout=0)
            self.page.wait_for_timeout(1000)

      def upload_image(self):
      # click on "File Upload" and upload the "Image"
            if self.assert_validate.validate_attributes(self,'fileupload', 'fileuploadinput', 'whiteboard_page'):
                  return
            self.fileupload.click(timeout=0)
            self.fileuploadinput.set_input_files(get_image_file_path())
            self.page.wait_for_timeout(10000)
            self.chatbox.click(timeout=0)
            self.message.fill("I uploaded Image and it's Loaded")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            
      def upload_pdf(self):  
      # click on "File Upload" and upload the "PDF"
            if self.assert_validate.validate_attributes(self,'fileupload', 'fileuploadinput', 'whiteboard_page'):
                 return
            self.fileupload.click(timeout=0)
            self.fileuploadinput.set_input_files(get_pdf_file_path())
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("I uploaded pdf and Pdf loaded")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(10000)
                  

      def spanish_language_popup(self):
      # select "Spanish Language"
            if self.assert_validate.validate_attributes(self,'selectlanguage', 'spanish_language', 'whiteboard_page'):
                 return 
            self.page.wait_for_timeout(1000) 
            self.selectlanguage.click(timeout=0)
            self.spanish_language.click(timeout=0) 
            self.page.wait_for_timeout(5000)
            self.sendchat.click()
            self.sendchat.fill("I have changed the language from English to Spanish ") 
            self.send_button.click()
            self.sendchat.click()
            self.sendchat.fill("You got Language popup ?") 
            self.send_button.click()
            self.page.wait_for_timeout(1000)

      def french_language_popup(self):
      # select "French Language"
            if self.assert_validate.validate_attributes(self,'selectlanguage', 'french_language', 'whiteboard_page'):
                 return 
            self.page.wait_for_timeout(1000) 
            self.selectlanguage.click(timeout=0)       
            self.page.wait_for_timeout(10000) 
            #self.orignal_lang.click(timeout=0) 
            self.selectlanguage.click(timeout=0)
            self.french_language.click(timeout=0) 
            self.page.wait_for_timeout(5000)
            self.fench_chat.click() 
            self.fench_chat.fill("I have changed the language from English to French")
            self.send_button.click()
            self.page.wait_for_timeout(1000)
      
      def WB_GoSlow_Button(self):
            self.GoSlow_button.click(timeout=0)
            self.page.wait_for_timeout(2000)
            self.chatbox.click(timeout=0)
            self.message.fill("You got a GoSlow Button Popup ?")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(2000)
      
      def WB_click_eraser_button(self):
            if self.assert_validate.validate_attributes(self,'Grid','eraser_button','whiteboard_page'):
                  return
            self.Grid.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.eraser_button.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.chatbox.click(timeout=0)
            self.message.fill("Eraser Working ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(2000)

      def WB_activate_smiley_tool(self):
            if self.assert_validate.validate_attributes(self,'smiley_button','smiley_one','whiteboard_page'):
                  return
            self.smiley_button.click(timeout=0)
            self.page.wait_for_timeout(2000)
            self.smiley_one.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(2000)
            self.smiley_button.click(timeout=0)
            self.smiley_two.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Smiley Working ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(2000)


      def WB_Colour_Button(self):
            if self.assert_validate.validate_attributes(self,'colour','red_colour','whiteboard_page'):
                  return

            self.colour.click(timeout=0)
            self.page.wait_for_timeout(1000)
            self.red_colour.click(timeout=0)
            self.WB_pencil()
      
      def WB_activate_zoom_in_out_tool(self):
            if self.assert_validate.validate_attributes(self,'zoom_min','reset_zoom','whiteboard_page'):
                  return         
            self.zoom_min.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Zoom In ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.reset_zoom.click(timeout=0)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Reset Zoom ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.zoom_out.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Zoom Out")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.reset_zoom.click(timeout=0)
            self.page.wait_for_timeout(1000)

      def WB_activate_undo_redo_tool(self):
            if self.assert_validate.validate_attributes(self,'zoom_min','reset_zoom','whiteboard_page'):
                  return 
            self.undo_button.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Undo button working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.redo_button.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Redo button working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)

      def WB_click_shapes_tool(self):
            if self.assert_validate.validate_attributes(self,'zoom_min','reset_zoom','whiteboard_page'):
                  return 
            self.shapes.click(timeout=0)
            self.pentagon.click(timeout=0)
            self.wbmouse.mouse.move(600, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(400, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Pentagon working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.shapes.click(timeout=0)
            self.heptagon.click(timeout=0)
            self.wbmouse.mouse.move(400, 300)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(200, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Heptagon working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.shapes.click(timeout=0)
            self.circle.click(timeout=0)
            self.wbmouse.mouse.move(300, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(200, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Circle working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)
            self.shapes.click(timeout=0)
            self.otagon.click(timeout=0)
            self.wbmouse.mouse.move(700, 350)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(600, 320)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(1000)
            self.chatbox.click(timeout=0)
            self.message.fill("Octagon working")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(1000)


      def WB_click_delete_button(self):
            if self.assert_validate.validate_attributes(self,'Grid','delete','whiteboard_page'):
                  return
                       
            self.Grid.click(timeout=0)
            self.wbmouse.mouse.move(800, 450)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(600, 430)
            self.wbmouse.mouse.up()
            self.page.wait_for_timeout(2000)
            self.delete.click(timeout=0)
            self.wbmouse.mouse.move(800, 450)
            self.wbmouse.mouse.down()
            self.wbmouse.mouse.move(600, 430)
            self.wbmouse.mouse.up()
            self.chatbox.click(timeout=0)
            self.message.fill("Delete button Working ")
            self.send_msg.press("Enter")
            self.page.wait_for_timeout(2000)



