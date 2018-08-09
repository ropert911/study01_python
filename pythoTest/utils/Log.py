import os
import logging
import logging.handlers


__all__ = [
    'set_log_level',
    'set_log_path',
    'debug',
    'info',
    'warn',
    'error',
    'critical',
]


def create_stream_handler(level):
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s [SKS-%(levelname)s] %(process)d %(filename)s %(funcName)s %(lineno)d:  %(message)s')
    handler.setFormatter(formatter)
    return handler


def create_rotating_handler(path):
    mkdirs(path)
    handler = logging.handlers.RotatingFileHandler(path,
                                                   maxBytes=2097152,
                                                   backupCount=10)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter( '%(asctime)s [SKS-%(levelname)s] %(process)d %(filename)s %(funcName)s %(lineno)d:  %(message)s')
    handler.setFormatter(formatter)
    return handler


def mkdirs(path):
    path = os.path.dirname(path)
    if not os.path.exists(path):
        os.makedirs(path)


class SksLog(object):
    LEVEL_CONF = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARN': logging.WARN,
        'ERROR': logging.ERROR
    }

    def __init__(self, level='WARN'):
        self.level = SksLog.LEVEL_CONF[level]
        self.log_dir =  '/opt/data/pyspark/logs'
        self.log_file = 'py.log'
        self.log_path = os.path.join(self.log_dir, self.log_file)
        self._logger = None
        self.level_can_be_changed = True
        self.log_path_can_be_changed = True

    def set_log_level(self, level):
        if not self.level_can_be_changed:
            return
        new_level = SksLog.LEVEL_CONF[level.upper()]
        if self.level != new_level:
            for i in self._logger.handlers:
                if type(i) == logging.StreamHandler:
                    i.setLevel(new_level)
                    self.level = new_level
                    self.level_can_be_changed = False
                    break

    def set_log_path(self, path=None, filename=None, remove_old_file=True):
        if not self.log_path_can_be_changed:
            return
        if path and path != self.log_dir:
            self.log_dir = path
        if filename and filename != self.log_file:
            self.log_file = filename
        new_path = os.path.join(self.log_dir, self.log_file)
        if self.log_path != new_path:
            if remove_old_file:
                for i in self._logger.handlers:
                    if type(i) == logging.handlers.RotatingFileHandler:
                        self._logger.removeHandler(i)
                        break
            self._logger.addHandler(create_rotating_handler(new_path))
            self.log_path = new_path
            self.log_path_can_be_changed = False

    @property
    def logger(self):
        if self._logger:
            return self._logger
        self._logger = logging.getLogger('sks_logger')
        self._logger.addHandler(create_stream_handler(self.level))
        self._logger.addHandler(create_rotating_handler(self.log_path))
        self._logger.setLevel(logging.DEBUG)
        return self._logger


log = SksLog()
set_log_level = log.set_log_level
set_log_path = log.set_log_path
debug = log.logger.debug
info = log.logger.info
warn = log.logger.warning
error = log.logger.error
critical = log.logger.exception

