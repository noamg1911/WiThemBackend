from Alerts.MovementAlert import MovementAlert
from SMSPackage.SMSSender import SMSService
from ElasticHandler.ElasticHandler import ElasticHandler

sms_sender = SMSService()
elastic_query_handler = ElasticHandler()

mov = MovementAlert()
alerters = [mov]


def user_query_to_contacts(user, contacts):
    query_result = elastic_query_handler.query_data("search-users", {'terms': {'id': user}})
    user_contacts = query_result[0]["_source"]["contacts"]
    for contact in user_contacts:
        for phone_number in contact.values():
            contacts.add(phone_number)


def sms_manager(anomaly):
    for anomaly_message in anomaly:
        contacts = set()
        for user in anomaly[anomaly_message]:
            user_query_to_contacts(user, contacts)
            sms_sender.send_sms(anomaly_message, contacts)


def check_alerters():
    for alerter in alerters:
        anomaly = alerter.check_anomaly()
        if anomaly:
            sms_manager(anomaly)
            alerter.sms_sent = True
