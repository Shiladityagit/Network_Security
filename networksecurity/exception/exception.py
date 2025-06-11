import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    def __init__(self, error_message, error_details: sys):
        self.error_message = error_message
        _, _, exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno if exc_tb else "Unknown"
        self.file_name = exc_tb.tb_frame.f_code.co_filename if exc_tb else "Unknown"


    def __str__(self):
        return (
            f"Error occurred in Python script: [{self.file_name}] "
            f"at line number: [{self.lineno}] "
            f"with error message: [{self.error_message}]"
        )