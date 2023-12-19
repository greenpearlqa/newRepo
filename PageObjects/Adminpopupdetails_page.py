import datetime
from PageObjects.date_page import Datepage

class SessionDetails:

    def __init__(self, page):
        # Initialize the SessionDetails class with a Playwright page object
        self.page = page

        # Expect a popup to appear and retrieve session info
        
        with page.expect_popup() as new_session_info:
            self.calendar_view = page.get_by_role("button", name="View Calendar")
        session_info = new_session_info.value
        session_info.wait_for_load_state()

        # Admin Schedule One-time plan
        self.select_date = session_info.locator('xpath = //button[@class="fev_monthview_cellbtn ng-scope fev_monthview_selected"]')
        session_info.on("dialog", lambda dialog: dialog.accept())
        self.select_pgm = session_info.locator("#ddlprogram")
        self.select_subject = session_info.locator("#ddlsubject")
        self.session_type = session_info.get_by_label("One-Time")
        self.select_comment = session_info.get_by_placeholder("I need help with.")
        self.add_comment = session_info.get_by_placeholder("I need help with.")
        self.time = session_info.locator("a")
        self.add_time = session_info.locator("div:nth-child(2) > .fev_timepicker > tbody > tr > td > .btn")
        self.schedule_session = session_info.get_by_role("button", name="Schedule")

        # Admin Schedule weekly plan
        self.enddatecalendar = session_info.get_by_role("button", name="").nth(1)
        self.enddate = session_info.locator('xpath=//button[@class="btn btn-sm btn-info uib-datepicker-current ng-binding"]')
        self.current_day = datetime.datetime.today().strftime('%A')
        self.select_current_day = session_info.get_by_label(self.current_day)

        # View session
        self.select_session = session_info.get_by_role("link", name="Math 6:00AM-6:15AM")
        self.select_session_popup = session_info.get_by_role("button", name="Cancel")
        self.viewcalendarclose = session_info



    def Accept_one_time_session_details(self):
        # Accept One-time session details
        self.select_date.click(timeout=0)
        self.select_pgm.select_option("string:0")
        self.select_subject.first.select_option("string:1")
        self.session_type.check(timeout=0)
        self.select_comment.click(timeout=0)
        self.add_comment.fill("Testing")
        self.time.first.dblclick(timeout=0)
        self.add_time.first.dblclick(timeout=0)
        return Datepage(self.page)

    def Accept_session_details_for_weekly(self):
        # Accept session details for a weekly plan
        self.select_date.click(timeout=0)
        self.select_pgm.select_option("string:0")
        self.select_subject.first.select_option("string:1")
        self.select_comment.click(timeout=0)
        self.add_comment.fill("Testing")
        self.enddatecalendar.click(timeout=0)
        self.enddate.click(timeout=0)
        self.select_current_day.check(timeout=0)
        return Datepage(self.page)

    def click_adminschedule(self):
        # Click the admin schedule button
        self.page.wait_for_timeout(5000)
        self.schedule_session.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.viewcalendarclose.close()

    # Uncomment the following method if needed
    """
    def session_info(self):
        # Perform actions related to session information
        # self.select_session.click()
        # self.select_session_popup.click()
        self.viewcalendarclose.close()
        return Publishsession(self.page)
    """

    def Accept_session_details_for_weekly_with_program(self):
        # Accept session details for a weekly plan
        self.select_date.click(timeout=0)
        self.select_pgm.select_option("string:13535")
        self.select_subject.first.select_option("string:1")
        self.select_comment.click(timeout=0)
        self.add_comment.fill("Testing")
        self.enddatecalendar.click(timeout=0)
        self.enddate.click(timeout=0)
        self.select_current_day.check(timeout=0)
        return Datepage(self.page)

    
