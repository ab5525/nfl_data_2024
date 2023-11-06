import logging
import sys



def create_logger(path='./output/my_log.txt', name= 'my_logger'):
    # Create a logger
    logger = logging.getLogger(__name__)

    # Set the logging level
    logger.setLevel(logging.DEBUG)

    # Create a file handler
    handler = logging.FileHandler(path)
    stdout_handler = logging.StreamHandler(stream=sys.stdout)

    # Set the logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(handler)
    logger.addHandler(stdout_handler)

    # Log a message
    logger.info('Logger initialized: '+ name)

    return logger
