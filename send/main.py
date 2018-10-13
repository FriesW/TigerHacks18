import sendEmail

##creds for gmail
login = 'tigerhacks2018Delta@gmail.com'
password = 'WESrY45@Ul1h'
verbose = True


##sanitize inputs
def emailCAS():
    
    ##get data for email
    to_addr = input('To: ')

    if(to_addr == ''):
        to_addr = 'tigerhacks2018Alpha@outlook.com'
        print(to_addr)

    from_addr = input('From: ')

    if(from_addr == ''):
        from_addr = 'tigerhacks2018Delta@gmail.com'
        print(from_addr)

    subject = input('Subject: ')

    if(subject == ''):
        subject = 'POW Test'
        print(subject)

    ##POW takes in a number or N for none.. no string defaults to 20
    powork = input('Proof of work level(0-30 or N for None): ')

    if(powork.isnumeric()):
        powork = int(powork)
    elif(powork == 'N'):
        powork = None
    else:
        powork = 20
        print(powork)

    ##message
    print('Message: ')
    message = input()

    if(message == ''):
        message = 'This a test email of POW'
        print(message)

    ##call email function / send
    sendEmail.sendemail(from_addr, to_addr, '', subject, message, powork, login, password, verbose, smtpserver='smtp.gmail.com:587')



def main():
    while(True):
        response = input('Would you like to send an email?(Y/N) ')
        if(response == 'y' or response == 'Y'):
            emailCAS()
        else:
            break
main()
