from modules.configuration.configuration_base import Parse_configuration_ciphers
from modules.server.testssl_base import Testssl_base


class Robot(Testssl_base):
    conf = Parse_configuration_ciphers(openssl="3.0.0", ciphers=["RSA"])
    """
    Analysis of the robot testssl results
    """
    # to override
    def _set_arguments(self):
        """
        Sets the arguments for the testssl command
        """
        self._arguments = ["-BB"]

    # to override
    def _worker(self, results):
        """
        The worker method, which runs the testssl command

        :param results: dict
        :return: dict
        :rtype: dict
        """
        return self._obtain_results(results, ["ROBOT"])
