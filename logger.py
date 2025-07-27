import logging

def setup_logger():
    logging.basicConfig(
        filename='user_logs.log',
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )
