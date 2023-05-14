# import logging
# import os
# from datetime import datetime

# LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
# logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
# os.makedirs(logs_path,exist_ok=True)

# LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

# # with open(LOG_FILE_PATH,'w'): pass

# logging.basicConfig(
#     filename=LOG_FILE_PATH,
#     format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
#     level=logging.INFO,
# )

# if __name__=="__main__":
#     logging.info("Logging has started")


import logging
from datetime import datetime
import os

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)


logging.basicConfig(format="%(asctime)s::%(levelname)s::%(message)s",
                    level=logging.INFO,
                    filename=LOG_FILE_PATH
                    )


# Define the logger instance
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Define the file handler and formatter
file_handler = logging.FileHandler(LOG_FILE_PATH)
formatter = logging.Formatter("%(asctime)s :: %(levelname)s :: %(message)s")
file_handler.setFormatter(formatter)

# Add the file handler to the logger instance
logger.addHandler(file_handler)

# logger.info("info log")
# logging.warning("this is warning log")
# logging.error("this is error log")

# logging.info(1)