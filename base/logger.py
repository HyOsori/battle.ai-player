import os
import logging
import random


class PlayerLogger(object):
    __instance = None

    @classmethod
    def __getinstance(cls):
        return cls.__instance

    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getinstance
        return cls.__instance

    def __init__(self):
        self._logger = logging.getLogger("player")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(levelname)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')

        import datetime
        now = datetime.datetime.now()
        import time
        timestamp = time.mktime(now.timetuple())

        dirname = './log'
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        file_name = "PlayerLog_%d.txt" % (random.randrange(1, 100))
        file_handler = logging.FileHandler(dirname + file_name)
        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def logger(self):
        return self._logger







