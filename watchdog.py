from Alerts.MovementAlert import MovementAlert
from SMSPackage.SMSSender import SMSService
from ElasticHandler.ElasticHandler import ElasticHandler

sms_sender = SMSService()
elastic_query_handler = ElasticHandler()

mov = MovementAlert()
alerters = [mov]


# def get_anomaly(alerter):
#     anomaly_state, anomaly_description = alerter.check_anomaly()
#     return anomaly_description if anomaly_state else None


def send_sms(content, contacts):
    sms_sender.send_sms(content, contacts)
    alerter.sms_sent = True


def anomaly_manager(alerter):
    anomaly = alerter.check_anomaly()
    if anomaly:
        for anomaly_message in anomaly:
            contacts = set()
            for user in anomaly[anomaly_message]:
                elastic_query_handler.query_data("search-users", "{'query': {'terms': {'_id': [{}] }}}".format(user))


def check_alerters():
    for alerter in alerters:
        anomaly_manager(alerter)
