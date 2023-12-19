from datetime import datetime
import os
from Utilities.paths import get_log_directory

class ExceptionHandling:
    
    def __init__(self):
        # Specify the directory where you want to save log files
        self.log_directory = get_log_directory()
        self.log_file_name = None  # Initialize log_file_name to None

    def create_log_file(self, custom_name=None):
        date_str = datetime.now().strftime("%Y-%m-%d")
        custom_name = custom_name or "default"  # Use custom_name if provided, otherwise use "default"
        sanitized_custom_name = ''.join(e for e in custom_name if e.isalnum() or e in ['_', '-'])  # Sanitize custom_name
        os.makedirs(self.log_directory, exist_ok=True)
        self.log_file_name = f"logs_{date_str}_{sanitized_custom_name}.txt"  # Assign the generated log file name

    def log_method_result(self, method, success, exception=None):
        if self.log_file_name is None:
            self.create_log_file()  # Create log file with default name if not provided
        
        log_file_path = os.path.join(self.log_directory, self.log_file_name)
        
        with open(log_file_path, "a") as f:
            if success:
                f.write(f"{method} ran successfully\n")
                # print(f"{method} ran successfully")
            else:
                f.write(f"{method} failed with exception: {exception}\n")
                # print(f"{method} failed with exception: {exception}")
