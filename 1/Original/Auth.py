class data(object):
    emailAndPassword = {'yellow@gmail.com':'password1234', 'red@gmail.com':'userPassword'}

def logIn(logEmail, logPassword):
    for email in data.emailAndPassword:
        if email == logEmail:
            if data.emailAndPassword[email] == logPassword:
                return True
            else: 
                return False