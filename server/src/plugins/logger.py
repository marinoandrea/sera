import logging

from .interfaces import Logger


class StdLogger(Logger):

    def __init__(self):
        logging.basicConfig(
            filename='debug.log',
            level=logging.DEBUG,
            format='[%(asctime)s] (%(levelname)s): %(message)s'
        )

    def log(self, lvl: str, msg: str):
        getattr(logging, lvl, 'info')(msg)
