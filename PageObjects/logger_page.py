from datetime import datetime
import logging
import os

from Utilities.paths import get_consolelog_directory

# Configure the logging
class customlogger:

    def __init__(self):
        # Specify the directory where you want to save log files
        self.consolelog_directory = get_consolelog_directory()
        self.log_file_path = None
    
    def create_console_log(self, custom_name=None):
        date_str = datetime.now().strftime("%Y-%m-%d")
        custom_name = custom_name or "default"  # Use custom_name if provided, otherwise use "default"
        sanitized_custom_name = ''.join(e for e in custom_name if e.isalnum() or e in ['_', '-'])  # Sanitize custom_name
        self.log_file_name = f"logs_{date_str}_{sanitized_custom_name}.txt"
        os.makedirs(self.consolelog_directory, exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,  # Set the logging level (adjust as needed)
            format='%(asctime)s - %(levelname)s - %(message)s',
            filename=os.path.join(self.consolelog_directory, self.log_file_name),
            filemode='a'
        )

        # Create a logger
        self.logger = logging.getLogger()

        # Create a console handler and set its log level
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)  # Set the log level for console output

        # Create a formatter and set it for the console handler
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)

        self.logger.addHandler(console_handler)
    
    def info(self, message):
        # Log an info message
        self.logger.info(message)
    
    def warning(self, message):
        # Log an info message
        self.logger.warning(message)
    
    def error(self, message):
        # Log an info message
        self.logger.error(message)
