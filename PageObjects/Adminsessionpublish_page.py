from datetime import datetime as dt, timezone
import pytz
from Utilities.assertion_validation import assertionandvalidation
import re

from Utilities.paths import download_bulksessionpublish_withtimeslot, download_publishsession_withtimeslot 

class Publishsession:

    def __init__(self, page):
        # Initialize the Publishsession class with a Playwright page object
        self.page = page
        self.adminschedule_page = assertionandvalidation()

        # Elements on the page
        self.session = page.get_by_role("link", name="  Session")
        self.daily_session_forecast = page.get_by_role("link", name="Daily Session Forecast", exact=True)
        #when publish with daily session forecast with network
        #self.daily_session_forecast_with_network = page.get_by_role("link", name="Daily Session Forecast With Network", exact=True)

        self.end_date = page.locator("#divEndDate span").nth(1)
        self.next_month = page.get_by_role("cell", name="»")
        self.username_field = page.locator("#txtStuUserName")
        self.enter_username = page.locator("#txtStuUserName")
        self.search = page.get_by_role("button", name="Search")
        self.publish = page.get_by_role("button", name="Publish", exact=True)
        
        self.modifyclick = page.locator(".category")
        # self.select_school = page.locator("#ddlSchool")
        self.category = page.locator("#ddlcategory")
        self.now = dt.now()
        self.time_str = self.now.strftime("%H:%M:%S")
        self.hours, self.minutes, self.seconds = self.time_str.split(":")
        self.starttimehour = page.locator("#ddlStartTimeHrsre")
        self.starttimemins = page.locator("#ddlStartTimeMinsre")
        self.duration = page.locator("#txtDurationre")
        self.tutor = page.locator("#txtTutorre")
        self.tutorenter = page.locator("#txtTutorre")
        self.select_tutor = page.get_by_text("qatesttutor30")
        self.tutorenterselect = page.locator("li").filter(has_text="qatesttutor30")
        self.submitclose = page.get_by_text("Submit").nth(1)
        self.select_user = page.get_by_role("row", name="All").get_by_role("checkbox")
        self.finish_publish = page.get_by_role("button", name="Finish Publish")
        
        self.unpublish = page.get_by_role("button", name="UnPublish", exact=True)
        self.select_student = page.locator("#chkAll")
        self.finish_unpublish = page.get_by_role("button", name="Finish UnPublish")

        # Daily session forecast with Time slot
        self.session_publish_withtimeslot = page.get_by_role("link", name="Daily Session Forecast With Time Slot")
        self.student_username = page.locator("#txtStuUserName")
        self.startdate_time = page.locator("#divStartDate span")
        self.date_starttime_hour= page.get_by_role("row", name="00 : 00").locator("span").first
        self.select_hour = page.locator('(//td[@class="hour"])[7]')        
        self.select_minute = page.get_by_role("cell", name="00").locator("span")
        self.set_min = page.get_by_role("cell", name="00")
        self.enddate = page.locator("#divEndDate span")
        self.enddate_hour= page.locator("span").filter(has_text=re.compile(r"^23$"))
        self.select_endhour= page.get_by_role("cell", name="06")
        self.set_endmin  = page.get_by_role("cell", name="59").locator("span")
        self.select_endminute = page.get_by_role("cell", name="30").nth(2)
        self.search_button = page.get_by_role("button", name="Search")
        self.select_all = page.locator("#chkAll")

        #Bulk Plan Publish With Time Slot
        self.publish_withtimeslot = page.get_by_role("link", name="Bulk Session Publish With Time Slot")
        self.bp_startdate = page.locator("#divStartDate span")
        self.bp_start_time = page.get_by_role("row", name="00 : 00").locator("span").first
        #self.bp_start_hour = page.get_by_role("cell", name="06")
        self.bp_start_hour = page.get_by_role("cell", name="18").nth(1)
        self.bp_start_minute = page.get_by_role("cell", name="00").locator("span")
        self.bp_set_min = page.get_by_role("cell", name="00")
        self.bp_enddate = page.locator("#divEndDate span")
        self.bp_select_enddate = page.locator("span").filter(has_text=re.compile(r"^23$"))
        #self.bp_end_hour = page.get_by_role("cell", name="06")
        self.bp_end_hour = page.get_by_role("cell", name="19").nth(1)
        
        self.bp_end_minute = page.get_by_text("59", exact=True)
        self.bp_set_endmin= page.get_by_role("cell", name="30").nth(2)
        self.bp_network_lable = page.get_by_text("Network", exact=True)
        self.bp_school = page.locator("#ddlSchool")
        self.publish_all= page.get_by_role("button", name="Publish All")
        self.ok_button = page.once("dialog", lambda dialog: dialog.accept())
       


    def fill_publish_session_details(self):
        # Click on elements and perform actions to fill in session details
        self.session.click(timeout=0)
        self.daily_session_forecast.click()

        #when publish with daily session forecast with network
        #self.daily_session_forecast_with_network.click()
        
        self.adminschedule_page.Dailysessionforcast_valid(self.page)
        self.username_field.click()
        self.enter_username.fill("Fevqastu1025")
        # self.select_school.select_option("222")
        self.search.click(timeout=0)
        self.publish.click(timeout=0)
        self.modifyclick.first.click()
        self.page.wait_for_timeout(3000)
        # Get the current time using the alias "dt"
        current_time = dt.now(timezone.utc)
        est_timezone = pytz.timezone("US/Eastern")
        est_time = current_time.astimezone(est_timezone)
        est_current_time = est_time.strftime("%H:%M:%S")
        hours, minutes, _ = est_current_time.split(":")

        # Select the options for hours and minutes based on the current time
        self.starttimehour.select_option(hours)
        self.page.wait_for_timeout(3000)
        self.starttimemins.select_option(f"00:{minutes}::00", timeout=100000)
        self.page.wait_for_timeout(3000)
        self.category.select_option("CourseWork_Help")
        self.page.wait_for_timeout(2000)
        self.duration.fill("30")
        # self.tutor.click()
        # self.tutorenter.fill("FevQAStu1024")
        # self.select_tutor.click(timeout=0)
        # self.page.wait_for_timeout(1000)
        # self.tutorenterselect.click()
        self.page.wait_for_timeout(2000)
        self.submitclose.click()
        self.select_user.check(timeout=0)
        self.finish_publish.click()
        self.page.wait_for_timeout(3000)
   
    def fill_unpublish_session_details(self):
        self.unpublish.click(timeout=0)
        self.select_student.check()
        self.finish_unpublish.click()
        self.page.wait_for_timeout(2000)
        
    def check_unpublish_success(self):
        # Get the value of the hidden field that holds the success message
        success_message_element = self.page.locator("#hdnFevResFevConstant290")
        success_message = success_message_element.get_attribute("value")

        # Validate if "Session unpublished successfully" is in the success message
        expected_success = "Un-publish will remove the session from application. Do you want to proceed?"
        if expected_success == success_message:
            print("Success message: Session unpublished successfully")
        else:
            print(f"Expected: '{expected_success}', Actual: '{success_message}'")
            assert False, "Expected success message not found"

    def fill_publish_session_details_with_TimeSlot(self):
        # Click on elements and perform actions to fill in session details
        self.session.click(timeout=0)
        self.session_publish_withtimeslot.click(timeout=0)
        self.student_username.click(timeout=0)
        self.student_username.fill("FevQAStu1020")
        self.startdate_time.click(timeout=0)
        self.date_starttime_hour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.select_hour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.select_minute.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.set_min.click(timeout=0)

        self.page.wait_for_timeout(2000)
        self.enddate.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.enddate_hour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.select_endhour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.set_endmin.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.select_endminute.click(timeout=0)
        self.page.wait_for_timeout(2000)
        
        self.student_username.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.search_button.click(timeout=0)
        self.page.wait_for_timeout(5000)
        self.page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        self.publish.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.select_all.check()
        self.finish_publish.click(timeout=0)
        self.page.wait_for_timeout(2000)
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Click Here To Download Result File").click()
        download = download_info.value
        download.save_as(download_publishsession_withtimeslot())
        self.adminschedule_page.dailysessionforecast_withTimeSlot_file_validation()

    def click_dialog(self):
        self.page.once("dialog", lambda dialog: dialog.accept())

    def bulkplan_publish_with_TimeSlot(self):
        self.session.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.publish_withtimeslot.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_startdate.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_start_time.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_start_hour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_start_minute.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_set_min.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_enddate.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_select_enddate.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_end_hour.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_end_minute.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_set_endmin.click(timeout=0)
        self.page.wait_for_timeout(2000)
        self.bp_network_lable.click(timeout=0)
        self.bp_school.select_option("18781")
        self.page.wait_for_timeout(3000)
        self.publish_all.click(timeout=0)
        self.page.wait_for_timeout(1000)
        self.click_dialog()
        self.ok_button
        self.page.wait_for_timeout(50000)
        
        with self.page.expect_download() as download_info:
            self.page.get_by_role("link", name="Click Here To Download Result File").click()
        download = download_info.value
        download.save_as(download_bulksessionpublish_withtimeslot())
        self.adminschedule_page.bulksessionpublish_withTimeSlot_file_validation()
        






