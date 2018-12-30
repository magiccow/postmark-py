import requests
import json

token = ''   # Your Postmark API token goes here
headers = {'user-agent': 'my-app/1.0', 'Accept': 'application/json', 'Content-Type': 'application/json','X-Postmark-Server-Token': '%s' % token}
# Make sure to add your registered 'From' address here:
data = json.dumps({'From': 'yourname@sender.com', 'To': 'theirname@recipient.com', 'Subject': 'Poem', 'HtmlBody': '<b>The boy stood on the burning deck</b>'})

r = requests.post('https://api.postmarkapp.com/email', headers=headers, data=data )

response = json.loads(r.text)
if response['ErrorCode'] == 0:
	print('Message ID = %s' % response['MessageID'])
else:
	print('Message not sent')

