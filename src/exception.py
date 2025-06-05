import sys
import logging

def error_message_detail(error,error_detail:sys):  #error_message_detail() – 📍 Get Exact Error Location
    _,_,exc_tb=error_detail.exc_info()  ## this give info about where error occured,on which line occured, in which file
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message[{2}]".format(
        file_name,exc_tb.tb_lineno,str(error))
    
    return error_message

class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message) #Without super().__init__(msg), Python won’t know what message to show when you print(e).
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

    def __str__(self):  ## print the error
        return self.error_message
    


            
        