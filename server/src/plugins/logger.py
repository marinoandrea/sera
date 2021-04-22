import logging

from .interfaces import Logger


class StdLogger(Logger):

    def __init__(self):
        logging.basicConfig(
            filename='debug.log',
            level=logging.DEBUG,
            format='[%(asctime)s] (%(levelname)s): %(message)s'
        )
        self.gunicorn_logger = logging.getLogger('gunicorn.error')

    def log(self, lvl: str, msg: str):
        getattr(logging, lvl, 'info')(msg)
        getattr(self.gunicorn_logger, lvl, 'info')(msg)
