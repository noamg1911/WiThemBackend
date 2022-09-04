from ElasticHandler.ElasticHandler import ElasticHandler


class Alert:
    """
    Master class for Alerts, used to check anomalys with elastic querys and sends the summarized results.
    """
    SMS_STRUCTURE = "{specific_alert}"
    def __init__(self):
        self.es = ElasticHandler()
        self.sms_sent = False
        self.state = False

    def check_anomaly(self):
        data = self._query_sensor()
        return self._summarized_results(data)

    def _query_sensor(self):
        raise "Function not used!"

    def _summarized_results(self, data_summary):
        raise "Function not used!"
