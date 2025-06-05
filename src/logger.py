# Python logging is a module that allows you to track events that occur while your program is running.
# You can use logging to record information about errors, warnings, and other events that occur during program execution. And logging is a useful tool for debugging, troubleshooting, and monitoring your program.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)



# ✅ Summary
# Part	                                       Purpose
# datetime.now().strftime(...)	      Creates a unique log file name
# os.makedirs(...)	                  Creates log directory if missing
# logging.basicConfig(...)	          Configures how logs are formatted and saved
# filename=...	                      Tells logger where to save the log file
# format=...	                      Controls how each log line looks