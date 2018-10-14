import smtplib

import sys
sys.path.append('../common')
import proof

##new line variable
nl = '\r\n'

##verbose flag just prints information about the email being sent

def sendemail(from_addr, to_addr, cc_addr,
              subject, message, powork,
              smtpserver, login, password,
              verbose = False):
    
    ##Addition of POW into header
    header = ''
    if(powork != None):
        header += 'X-work-proof: {0}'.format(proof.pow(powork,to_addr.encode()).decode("utf-8")) + nl
    ##formation of headers
    header += 'From: {0}'.format(from_addr) + nl
    header += 'To: {0}'.format(to_addr) + nl #','.join(to_addr_list) + nl
    header += 'Cc: {0}'.format(cc_addr) + nl #','.join(cc_addr_list) + nl
    header += 'Subject: {0}'.format(subject) + nl + nl
    message = header + message

    #connect to server / login
    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr, message)
    if(verbose == True):
        print(powork)
        print(problems)
        print(header)
    server.quit()
    return problems



##test variables
from_addr = 'tigerhacks2018Delta@gmail.com'
to_addr = 'tigerhacks2018Alpha@outlook.com'                                         
login = 'tigerhacks2018Delta@gmail.com'
password = 'WESrY45@Ul1h'
subject = 'test'
message = 'my stuff'

##lists?
to_addr_list = ['winters.john@gmail.com']


#run code
#sendemail(from_addr, to_addr, '', subject, message, login, password)
