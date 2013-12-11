__author__ = 'mishy'

import logging


class PdfLogger(object):
    """
    General use logger for Figdocs

    @TODO get this production ready
    """

    @staticmethod
    def write_info(msg):
        """Write an info line to the log"""
        logging.info(msg)

    @staticmethod
    def write_error(msg):
        """Write an error to the log"""
        out = "Timestamp " + msg
        logging.error(out)

    @staticmethod
    def everything_went_wrong(self):
        """For major problems where the server can no longer function"""
        self._writeError("Oh nooooooooooo")

    @staticmethod
    def _send_to_i():
        """Write log to the i"""
        return None

    @staticmethod
    def _end_log(self):
        # not sure we have to do much here
        self.writeInfo("======================")
        self.writeInfo("ENDING LOG" + "timestamp")
        self.writeInfo("======================")

    @staticmethod
    def _create_log():
        # need to add the date to the filename
        logging.basicConfig(filename='test.log',level=logging.DEBUG)

    def __init__(self):
        self._create_log()