import os
import logging
import datetime
from .log_config import ConfigLogger


class LoggerManager():
    def __init__(self):
        # instantiate the instance of the class
        self.config = ConfigLogger.config
        # get the array of handers. DEBUG, ERROR
        self.log_handlers = self.initialize_log_handlers()
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
    # function to import the modules

    def load_module_func(self, module_name):
        mod = __import__('%s' % (module_name), fromlist=[module_name])
        return mod

    # function to create a new directory if the log directory is not available
    def get_log_directory(self):
        # get current path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        parent_dir = os.path.dirname(current_dir)
        log_dir = os.path.join(parent_dir, 'Logs')

        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        return log_dir

    # method to get the name of the files to be saved or is saved
    def get_log_filename(self, prefix=None):
        # change the name if you want. I am lazy with names
        user_id = "FIVE_MIN_MONGO_SCRIPT_LOGFILE"
        current_date = datetime.datetime.now().strftime('%Y%m%d')
        log_filename = f"log_{user_id}_{current_date}.log"

        if prefix is not None:
            log_filename = f"{prefix}_log_{user_id}_{current_date}.log"

        logs = os.path.join(self.get_log_directory(), log_filename)
        return logs

    def initialize_log_handlers(self):
        log_handlers = []

        for k, v in self.config['handlers'].items():
            t_import = v.get('import', None)
            t_class = v.get('class', None)
            # params for the files
            t_params = v.get('params', {})
            # log levels (DEBUG, INFO, ERROR, CRITICAL etc)
            t_level = v.get('level', None)
            t_formatter = v.get('formatter', None)
            t_prefix = v.get('prefix', None)

            if t_formatter != 'None':
                t_formatter = logging.Formatter(t_formatter)

            h_instance = None
            # file and _file for backups
            if k == 'info_file' or k == 'error_file':
                # set the filenames
                t_params['filename'] = self.get_log_filename(t_prefix)

            mod = self.load_module_func(t_import)
            h_instance = getattr(mod, t_class)(**t_params)

            if t_level != 'NONE':
                h_instance.setLevel(t_level)
                h_instance.setFormatter(t_formatter)

            logging.getLogger().addHandler(h_instance)
            log_handlers.append(h_instance)

        return log_handlers

    def _log(self, level, message):
        self.logger.log(level, message)

    def getMessage(self, messages):
        log = [str(message) for message in messages]
        message = ', '.join(log)
        return message

    def info(self, *messages, filename=None):
        message = self.getMessage(messages)
        if filename:
            message = f"[{filename}] - {message}"
        self._log(logging.INFO, message)

    def debug(self, *messages):
        message = self.getMessage(messages)
        self._log(logging.DEBUG, message)

    def error(self, *messages, filename=None, line=None):
        message = self.getMessage(messages)
        if filename and line:
            message = f"[{filename}:{line}] - {message}"
        self._log(logging.ERROR, message)