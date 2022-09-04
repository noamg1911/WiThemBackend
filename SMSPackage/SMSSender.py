from twilio.rest import Client 

class SMSService():
    def __init__(self, account_sid='AC05e935c3feac76bdb3ef99ec10cec160', auth_token='c8cdee635fcde51d991f4025cb6e09df', messaging_service_sid='MGe28a85bd5d84d5a4cf703e9693cb8074'):
        """
            Initalizes the twilio client
            @param account_sid: use default unless we run out of money 
            @param auth_token
            @param messaging_service_sid 
        """
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.messaging_service_sid = messaging_service_sid
        self.twilio_client = Client(self.account_sid, self.auth_token) 

    def send_sms(self, content, phone_numbers):
        """
            This function exports the sms sending for the backend agent

            @param content: the content of the sms message, possibly unicode
            @param phone_numbers: list of phone number to send to, should be a string with the following format '+972..' 
        """
        for phone_num in phone_numbers:
            message = self.twilio_client.messages.create(  
                                  messaging_service_sid=self.messaging_service_sid, 
                                  body=content,      
                                  to=phone_num 
                              )