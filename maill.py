import smtplib
person=raw_input('mail_id:')
h="Subject:hii"
msgg=h+'\n'+raw_input("message:")


server=smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()

server.login('shbakrys@gmail.com','stunner1')
server.sendmail('shbakrys@gmail.com',person,msgg)
server.close()
# import smtplib

# to = raw_input"enter the email:"
# gmail_user = 'shbakrys@gmail.com'
# gmail_pwd = 'stunner1'
# smtpserver = smtplib.SMTP("smtp.gmail.com",587)
# smtpserver.ehlo()
# smtpserver.starttls()
# smtpserver.ehlo() # extra characters to permit edit
# smtpserver.login(gmail_user, gmail_pwd)
# header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:testing \n'
# print header
# msg = header + '\n this is test msg from mkyong.com \n\n'
# smtpserver.sendmail(gmail_user, to, msg)
# print 'done!'
# smtpserver.quit()
