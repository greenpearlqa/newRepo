from csv import reader
import csv
import time
from Utilities.paths import download_excel_file_path

class DownloadExcelData:

    def __init__(self,page):
        self.page = page
        time.sleep(5)
        with page.expect_download() as download_info:
            page.get_by_role("link", name="Click Here To Download Result File").click()
        download = download_info.value
        downloadfilepath = download_excel_file_path()
        download.save_as(downloadfilepath)
        #with open('C://Users//jeethendra.hb//Desktop//jeethendra1//Download_Data//publsihedResult.csv', 'r', encoding="cp437", errors='ignore') as file:
        ##   print(data)