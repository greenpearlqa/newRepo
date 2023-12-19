

class DeleteSelfSchedulSesson:

    def __init__(self, page):
    # Initialize the SelfSchedule class with a Playwright page object
      self.page = page
      self.myschedule = page.get_by_role("link", name=" My Schedule")
      self.delete_plan = page.locator('(//a[@class="ng-binding ng-scope fev_monthview_primary_with_event_normal"])[1]')
      self.delete_plan_button = page.get_by_role("button", name="Delete Plan")
      self.session_one = page.locator('(//a[@class="ng-binding ng-scope fev_monthview_primary_with_event_normal"])[1]')



    def select_mySchedule_plan(self):
    #Select My Schedule plan.
       self.page.wait_for_timeout(4000)
       self.myschedule.click(timeout=0)


    def delete_selfSchedule_plan(self):
    #  Delete plans for a single session.
       self.page.wait_for_timeout(2000)
       self.delete_plan.click(timeout=0)
       self.page.wait_for_timeout(3000)
       self.delete_plan_button.click(timeout=0)
       self.page.wait_for_timeout(4000)
       self.myschedule.click(timeout=0)
       self.page.wait_for_timeout(2000)

    def delete_All_selfSchedule_plan(self, num_repeats=4):
       # Delete plans for multiple sessions
       for _ in range(num_repeats):
        self.myschedule.click(timeout=0)
        self.session_one.click(timeout=0)
        self.delete_plan_button.click(timeout=0)
        self.page.wait_for_timeout(5000)
       
       
        
        
       
       

       
