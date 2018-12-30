import requests
import json
import time
import sys

if len(sys.argv)>1:
	messageID = sys.argv[1]
else:
	messageID = ''
	

token = ''    # Your Postmark API token goes here
headers = {'user-agent': 'my-app/1.0', 'Accept': 'application/json', 'Content-Type': 'application/json','X-Postmark-Server-Token': '%s' % token}

r = requests.get('https://api.postmarkapp.com/messages/outbound/%s/details' % messageID, headers=headers)

response = json.loads(r.text)

status = response['Status']
if status == 'Sent':
	for event in response['MessageEvents']:
		print(event['Type'])     # 'Delivered', 'Bounced'
		print(event['ReceivedAt'])
else:
	print('Status = %s' % status)


			
