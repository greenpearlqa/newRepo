# Verify Delete plan for Admin schedule

class DeleteScheduleSessionpage:

    def __init__(self, page):

        # Initialize the Adminsessionpage class with a Playwright page object
        self.page = page

        # Expect a popup to appear and retrieve session info
        
        with self.page.expect_popup() as new_admin_session_info:
            self.calendar_view = page.get_by_role("button", name="View Calendar")
        admin_session_info = new_admin_session_info.value
        admin_session_info.wait_for_load_state()

        #self.today_day = session_info.locator('//button[@class="btn btn-primary"]')
        
        self.today_session =admin_session_info.locator('(//a[@class="ng-scope fev_monthview_primary_with_event_normal"])[1]"]')
        self.delete_plan_button = admin_session_info.locator('//button[@class="btn btn-danger pull-left ng-scope"]')
        self.all_todays_session = admin_session_info.locator('(//a[@class="ng-scope fev_monthview_primary_with_event_normal"])[1]')
        self.close_calender = admin_session_info

    def delete_session(self):
        
        #self.today_day.click(timeout=0)
        self.today_session.click(timeout=0)
        self.delete_plan_button.click(timeout=0)
        self.page.wait_for_timeout(3000)
        self.page.reload(wait_until='load')
        self.page.wait_for_timeout(5000)
        #self.close_calender.close()

    def delete_All_schedule_session(self, num_repeats=4):
        for _ in range(num_repeats):
            self.all_todays_session.click(timeout=0)
            self.delete_plan_button.click(timeout=0)
            self.page.wait_for_timeout(3000)
            self.page.reload(wait_until='load')
            self.page.wait_for_timeout(5000)

