import smtplib, time, imaplib, email

Email = 'yourusername@gmail.com'
Password = 'your password'

def get_last_msg():
	mail = imaplib.IMAP4_SSL('imap.gmail.com')
	mail.login(Email, Password)
	mail.select('inbox')
	result, data = mail.uid('search', None, "ALL")
	i = len(data[0].split())
	for x in range(i):
		latest_email_uid = data[0].split()[x]
		result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
		raw_email = email_data[0][1]
	raw_email_string = raw_email.decode('utf-8')
	for line in raw_email_string.split('\n'):
		if 'From:' in line:
			sender = line.split(':')[1].rstrip()
		if 'Date:' in line:
			x = line.split(' ')
			date = str(x[3])+' '+str(x[2])+' '+str(x[4])
			time = str(x[5])
	email_message = email.message_from_string(raw_email_string)
	for part in email_message.walk():
		if part.get_content_type() == "text/plain":
			body = part.get_payload(decode=True)
			msg = body.decode('utf-8')
		else:
			continue
	return {'sender':sender,'message':msg,'date':date,'time':time}

def await_response():
	last_message = get_last_msg()
	new = None
	while new == None:
		check = get_last_msg()
		if check['sender'] == last_message['sender']:
			if check['time'] != last_message['time']:
				new = check
	return new

def send(recipient,msg):
	server = smtplib.SMTP('smtp.gmail.com', 587)
	try:
		server.sendmail(Email, recipient, msg)
	except:
		server.ehlo()
		server.starttls()
		server.login(Email, Password)
		server.sendmail(Email, recipient, msg)
