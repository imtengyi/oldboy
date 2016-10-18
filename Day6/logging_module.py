#!/usr/bin/env python3
__auther__ = 'dmmjy9'

import logging

# logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
# logging.debug("This is a debug log")
# logging.warning("This is a warning log")
# logging.critical("This is a critical log")

#create logger
logger = logging.getLogger('TEST-LOG')
logger.setLevel(logging.DEBUG)

#create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

#create file handler and set level to warning
fh = logging.FileHandler("access.log")
fh.setLevel(logging.WARNING)

#create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - (levelname)s - %(message)s')

#add formatter to ch and fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)

#add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

#'application' code
logger.debug("This is a debug log")
logger.info("This is a info log")
logger.warning("This is a warning log")
logger.error("This is a error log")
logger.critical("This is a critical log")
