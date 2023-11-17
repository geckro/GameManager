import logging

log_filename = 'log.log'
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging_levels = ('info', 'warning', 'error')

logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format=log_format
)


def log(level: str, message: any):
    """
        Log a message with the specified severity level
        Parameters:
        - level (str): The severity level of the log ('info', 'warning', 'error')
        - message (str): The message to be logged
    """

    if level not in logging_levels:
        logging.warning(f"Unknown logging level: {level}")
        return

    message = str(message)

    if level.lower() == 'info':
        logging.info(message)
    elif level.lower() == 'warning':
        logging.warning(message)
    elif level.lower() == 'error':
        logging.error(message)
