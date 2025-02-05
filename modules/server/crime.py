from modules.configuration.configuration_base import (
    Parse_configuration_checks_compression,
)
from modules.server.testssl_base import Testssl_base
import logging


class Crime(Testssl_base):
    conf = Parse_configuration_checks_compression(openssl="1.1.0")

    """
    Analysis of the crime testssl results
    """

    # to override
    def _set_arguments(self):
        """
        Sets the arguments for the testssl command
        """
        self._arguments = ["-C"]

    # to override
    def _worker(self, results):
        """
        The worker method, which runs the testssl command

        :param results: dict
        :return: dict
        :rtype: dict
        """
        return self._obtain_results(results, ["CRIME_TLS"])
