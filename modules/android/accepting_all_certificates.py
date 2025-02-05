from modules.android.super_base import Super_base
from utils.logger import Logger


class Accepting_all_certificates(Super_base):
    """
    Check if the apk accepts all certificates.

    """

    def _get_logger(self):
        """
        Logger for the android module.

        """
        return Logger("Accepting all SSL certificates")

    # to override
    def _set_arguments(self):
        """
        Arguments for the android module.
        """
        self._arguments = []

    # to override
    def _worker(self, results):
        """
        Run the module.

        :param results: dict of Result
        :type results: dict
        :return: dict results of the module
        :rtype: dict
        """
        return self._obtain_results(
            results, ["Accepting all SSL certificates"], ["criticals"]
        )
