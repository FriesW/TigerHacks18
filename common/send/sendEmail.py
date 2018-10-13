import smtplib
import proof
nl = '\r\n'

def sendemail(from_addr, to_addr, cc_addr,
              subject, message,
              login, password,
              smtpserver='smtp.gmail.com:587'):
    
    ##Addition of POW into header
    header = 'X-work-proof: {0}'.format(proof.pow(20,to_addr.encode()).decode("utf-8")) + nl
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
    problems = server.sendmail(from_addr, to_addr_list, message)
    #print(problems)
    server.quit()
    return problems



##test variables
from_addr = 'tigerhacks2018Delta@gmail.com'
to_addr = 'winters.john@gmail.com'                                         
login = 'tigerhacks2018Delta@gmail.com'
password = 'dxF$5DzV580q'
subject = 'test'
message = 'icles'

##lists?
to_addr_list = ['winters.john@gmail.com']


#run code
sendemail(from_addr, to_addr, '', subject, message, login, password)
