import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s',
                    datefmt='%m/%d/%Y %H:%M:%S')
logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")

# Create your own logger and then import it

stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log')

stream_h.setLevel(logging.WARNING)
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning("This is warning")
logger.error('This is error')

import traceback
from logging.handlers import RotatingFileHandler

try:
    a = [1, 2, 3]
    val = a[4]
except IndexError as e:
    logging.error("The error is %s", traceback.format_exc())

#python json logger refer for get logger file as json