from ElasticHandler.ElasticHandler import ElasticHandler

class Alert():
    def __init__(self):
        self.es = ElasticHandler()
        self.sms_sent = False
        self.state = False

    def check_anomaly(self):
        raise("Function not used!")

    def _update_alert(self):
        raise("Function not used!")
