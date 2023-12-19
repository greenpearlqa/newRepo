

import openpyxl
from Utilities.paths import download_OverlapBulkplanfile_path

class BulkPlanOverlapped:
        
        

        def overlap_bulkplan_result_file_validation(self):
            result_file_path = download_OverlapBulkplanfile_path()
            bulkplan_wb = openpyxl.load_workbook(result_file_path)
            result_file_sheet_name = "BulkUploadResult"  # Actual sheet name
            bulk_plan_result = bulkplan_wb[result_file_sheet_name]
            result_cell_value = str(bulk_plan_result.cell(row=2, column=1).value)

            if "successful" in result_cell_value.lower():
                print(f"Bulk Session schedule successful with message: {result_cell_value}")
            elif "Overlapped plan timeslot" in result_cell_value:
                print(f"Overlap detected: {result_cell_value}")
            else:
                print(f"Bulk session schedule failed with message: {result_cell_value}")

            bulkplan_wb.close()

