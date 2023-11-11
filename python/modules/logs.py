import logging
import logging.config

# severity levels
# logging.debug('This is a debug message')
# logging.info('This is info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# logging.basicConfig(level=logging.DEBUG)
# logging.debug('This will be logged')

# writes to a file
# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
# logging.warning('This will be logged to a file')


# add date and time
# logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
# logging.info('Admin logged in')

# change time formant
# logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
# logging.warning('Admin logged out')


# loggin variable data
# name = 'John'

# logging.error('%s raised an error', name)

# or

# import logging

# name = 'John'

# logging.error(f'{name} raised an error')


# capturing stack traces (actions, functions before the errot occures)
# a = 5
# b = 0

# try:
#     c = a / b
# except Exception as e:
#     logging.error('Exception occured', exc_info=True)

# or

# try:
#   c = a / b
# except Exception as e:
#   logging.exception("Exception occurred")


# creating a custom logger
# logger = logging.getLogger('example_logger')
# logger.warning('This is a warning')



# HANDLERS (sending log to different places)
# logger = logging.getLogger(__name__)

# Create handlers
# c_handler = logging.StreamHandler()
# f_handler = logging.FileHandler('file.log')
# c_handler.setLevel(logging.WARNING)
# f_handler.setLevel(logging.ERROR)

# # Create formatters and add it to the handlers
# c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
# f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# c_handler.setFormatter(c_format)
# f_handler.setFormatter(f_format)

# # Add handlers to the logger
# logger.addHandler(c_handler)
# logger.addHandler(f_handler)

# logger.warning('This is a warning')
# logger.error('This is an error')



# Configuration methods (import from config file)

logging.config.fileConfig(fname = 'file.conf', disable_existing_loggers=False)

# Get the logger specified in the file
logger = logging.getLogger(__name__)

logger.debug('This is a debug message')