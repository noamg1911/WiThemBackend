from twilio.rest import Client 
 
account_sid = 'AC05e935c3feac76bdb3ef99ec10cec160' 
auth_token = '31948c701a95e09663c74188ca6cd036' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MGe28a85bd5d84d5a4cf703e9693cb8074', 
                              body='Test',      
                              to='+972544682462' 
                          )
 
print(message.sid)