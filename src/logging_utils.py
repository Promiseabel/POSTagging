import logging
from logging.handlers import RotatingFileHandler
import os

def get_logger(name, log_file='project.log', max_bytes=5_000_000, backup_count=5):
    """
    Create a logger with handlers for both file and console output.
    
    Parameters:
    - name: The name of the logger, typically `__name__` of the module.
    - log_file: The file path to write log messages.
    - max_bytes: Maximum file size for rotating logs (default: 5 MB).
    - backup_count: Number of backup files to keep for rotating logs (default: 5).
    
    Returns:
    - logger: Configured logger instance.
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # Set the default logging level to DEBUG

    # Check if the logger already has handlers (to prevent duplicate logs)
    if not logger.hasHandlers():

        #Reset/Create the log file
        with open(log_file, 'w'):
            pass

        # Create a rotating file handler to manage log file size
        file_handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler for immediate output to the terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create formatters and add them to handlers
        file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')

        file_handler.setFormatter(file_formatter)
        console_handler.setFormatter(console_formatter)

        # Add handlers to the logger
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
