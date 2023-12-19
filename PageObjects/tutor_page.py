from playwright.sync_api import expect

class Tutorpage:
        
            def __init__(self,page):
                self.page = page
                self.online = page.locator('//input[@type="submit" and @name="button" and @value="Go Online"]')
                #self.online = page.wait_for_selector('//input[@type="submit" and contains(@onclick, "checkOnlineOffLineStatus(true")]')
                #self.online = page.locator("input[name=\"button\"]")
                #self.online_button = page.locator('(//input[@class="btn btn-warning"])[1]')

                self.joinnowbutton_adminsession=page.locator('//input[@class="btn btn-join "]')                
                # self.adminjoin = page.get_by_role("button", name="Join Now")
                self.adminonline = page.locator('//input[@id="btnGoOnlineMaster"]')
                self.adminjoinnow = page.locator('//input[@id="btnJoinNow"]')
                self.joinnow = page.locator("#popupBtnJoinNow").get_by_role("button", name="Join Now")
                self.ondemandrequest = page.locator('#dyn_1 > div.panel-heading > h5 > a > i')
                self.ondemandjoinnow = page.get_by_role("button", name="Join Now")
                self.ondemand_session_request = page.locator('(//a[@class="accordion-toggle"])[2]')
                # self.ondemandjoinnow = page.locator('input.btn.btn-join[id="btnJoinNow"][studentname="Test 131"]')

                #New tutor dashboard changes
                self.onlinebutton = page.get_by_role("heading", name="Dashboard Go Online Go Offline").locator("span").first
                self.ondemandsession = page.locator("//a[@href='#divOnDemandCollapse']")
                self.Assigned = page.locator('text="Assigned"')
                self.preferredstudents = page.locator("//a[@href='#divpreferstudentsCollapse']")

                # Element for staging site tutor dashboard

                self.staging_goonline_button = page.get_by_role("heading", name="Dashboard Go Online Go Offline").locator("span").nth(2)
                self.staging_ondemand = page.get_by_role("link", name="OnDemand 1")
                self.staging_joinnow = page.get_by_role("button", name="Join Now")

                #Tutor offline after providing feedback
                self.dashboard = page.get_by_role("link", name=" Dashboard")
                self.offline = page.get_by_role("button", name="Go Offline")

                #Performance site New Tutor Dashboard(ondemand)
                self.performance_goonline_button = page.get_by_role("heading", name="Dashboard Go Online Go Offline").locator("span").nth(2)
                self.performance_ondemand = page.get_by_role("link", name="OnDemand 1")
                #self.performance_joinnow = page.get_by_role("button", name="Join Now")
                self.performance_joinnow= page.locator('//input[@id="btnJoinNow"]')
                self.prog_join_now = page.locator('//input[@id="btnJoinNowTop"]')
                

                #Performance site New Tutor Dashboard(admin)
                self.performance_admin = page.get_by_role("link", name="Assigned 0")
                self.performance_admin_joinnow = page.get_by_role("dialog", name="Aggregates").locator("#btnJoinNow")

            def click_tutor_func(self):
                self.online.first.click()
                
            '''
            def click_grp_tutor_func(self):
                if self.online.first.is_visible():
                    self.online.first.click(timeout=0)
                else:
                    self.joinnow.click()
            '''                         
            def tutor_joinnow(self):
                self.joinnow.click(timeout=0)
                    #return TutorWB(self.page)
            
            def tutor_admingoonline(self):
                self.page.wait_for_timeout(3000)
                self.adminonline.click()

            def tutor_joinnow_adminsession(self):
                 self.page.wait_for_timeout(3000)
                 self.joinnow.first.click(timeout=0)
                 #self.page.wait_for_timeout(3000)
              
            def tutor_joinnow_selfsession(self):
                self.joinnow.click(timeout=0)
            
            # def click_grp_tutor_func(self):
            #     if self.online.first.is_visible():
            #         self.online.first.click()
            #     else:
            #         self.joinnow.click()
            
            def click_tutor_online(self):
                # if self.online.is_visible() or self.online.first.is_enabled():
                self.online.first.click(timeout=0)
                self.page.wait_for_timeout(2000)
                self.ondemand_session_request.click(timeout=0)
                self.page.wait_for_timeout(2000)
                #self.ondemandrequest.click(timeout=0)
                self.ondemandjoinnow.first.click(timeout=0)
                # self.page.wait_for_timeout(3000)
                #return TutorWB(self.page)
            
            #New tutor dashboard changes Actions
            def tutor_online(self):
                self.onlinebutton.click(timeout=0)
                self.page.wait_for_timeout(5000)
            
            def tutor_ondemand(self):
                self.ondemandsession.click(timeout=0)
                self.page.wait_for_timeout(5000)
            
            def tutor_ondemand_joinnow(self):
                 self.ondemandjoinnow.click(timeout=0)
            
            def tutor_assigned(self):
                self.Assigned.click(timeout=0)
                self.page.wait_for_timeout(5000)
            
            def tutor_preferredstudents(self):
                self.preferredstudents.click(timeout=0)
                self.page.wait_for_timeout(5000)

            def stagingsite_click_tutor_online(self):
                self.staging_goonline_button.click(timeout=0)
                self.page.wait_for_timeout(1000) 
                self.staging_ondemand.click(timeout=0)
                self.page.wait_for_timeout(2000) 
                self.staging_joinnow.click(timeout=0)

            def tutor_offline(self):
                self.page.wait_for_timeout(2000)
                self.dashboard.click(timeout=0)
                self.page.wait_for_timeout(2000)
                self.page.once("dialog", lambda dialog: dialog.accept())
                self.offline.click(timeout=0) 

            def performancesite_click_tutor_online_ondemand(self):
                self.performance_goonline_button.click(timeout=0)
                self.page.wait_for_timeout(1000) 
                self.performance_ondemand.click(timeout=0)
                self.page.wait_for_timeout(3000) 
                self.performance_joinnow.click(timeout=0)
                #self.page.wait_for_timeout(2000) 
                #self.prog_join_now.click(timeout=0) 

            def performancesite_click_tutor_online_admin(self):
                self.performance_goonline_button.click(timeout=0)
                self.page.wait_for_timeout(1000) 
                self.performance_admin.click(timeout=0)
                self.page.wait_for_timeout(30000) 
                self.performance_admin_joinnow.click(timeout=0)
