from Alerts.MovementAlert import MovementAlert
from SMSPackage.SMSSender import SMSService
from ElasticHandler.ElasticHandler import ElasticHandler

sms_sender = SMSService()
elastic_query_handler = ElasticHandler()

mov = MovementAlert()
alerters = [mov]


def user_query_to_contacts(user: str, contacts: set) -> None:
    """
    queries the elastic DB for a specific user and parses the result for his relevant contacts' numbers
    :param user: the user to query his contacts
    :param contacts: the list of contacts to send an SMS to
    """
    query_result = elastic_query_handler.query_data("search-users", {'terms': {'id': user}})
    user_contacts = query_result[0]["_source"]["contacts"]
    for contact in user_contacts:
        for phone_number in contact.values():
            contacts.add(phone_number)


def sms_manager(anomaly: dict) -> None:
    """
    goes over anomaly messages and sends SMSs accordingly
    :param anomaly: the anomaly to go over
    """
    for anomaly_message in anomaly:
        contacts = set()
        for user in anomaly[anomaly_message]:
            user_query_to_contacts(user, contacts)
            sms_sender.send_sms(anomaly_message, contacts)


def check_alerters() -> None:
    """
    checks alerters for anomalies
    """
    for alerter in alerters:
        anomaly = alerter.check_anomaly()
        if anomaly:
            sms_manager(anomaly)
            alerter.sms_sent = True
