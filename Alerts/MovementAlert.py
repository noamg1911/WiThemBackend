import datetime
from Alerts.Alert import Alert

ITERATION_TIME = 30 * 60
ALERT_MESSAGE = "Phone hasn't been moved in a long time."


class MovementAlert(Alert):
    """
    Used to send specific gyro related alerts.
    """
    def __init__(self):
        super().__init__()

    def _query_sensor(self):
        """
        Querys events from the last iteration which are related to gyroscope sensors
        """
        current_time = int(datetime.datetime.timestamp(datetime.datetime.now()))
        data = self.es.query_data("search-event", {"bool": { "must": [{
                                                                  "match": {
                                                                    "Sensor": "Gyroscope"
                                                                  }},
                                                                {
                                                                  "range": {
                                                                    "Timestamp": {
                                                                        "gte": current_time - ITERATION_TIME
                                                                        }
                                                                  }
                                                                }]}})
        return data if data is not {} else None

    def _summarized_results(self, data_summary):
        """
        Summarizes the results and sends them with the correct SMS message.
        :param data_summary:
        :return:
        """
        if data_summary is not None:
            agent_ids = []
            for event in data_summary:
                agent_ids.append(event['_source']['AgentID'])
            return {self.SMS_STRUCTURE.format(specific_alert=ALERT_MESSAGE): list(set(agent_ids))}
        return None
