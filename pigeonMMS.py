#!/usr/bin/python



#          /
#  *//////{<>==================-
#          \
#
#  Author : HD Dananjaya (@_hddananjaya)
#  Web    : https://hddananjaya.wordpress.com
#  Date   : 30 June 2018
#
#
# import required libs
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
import smtplib
import sys, getopt


def usage():

	usageBanner = """
Usage : pigeonMMS.py <options>

  	-s : Sender name/number
  	-r : Receiver address
  	-m : Message
  	-h : Print usage

Example :	  	
pigeonMMS.py -s BOB -r +1234567890@mms.gateway.of.isp -m 'You are awesome!'
	"""
	print (usageBanner)



def main(argv):

   # default config for fastmail.com
   SERVER_ADDR = "smtp.fastmail.com"
   SERVER_PORT = 587
   USERNAME = "<emailaddress>"
   PASSWORD = "<apppassword>"

   sender = ""
   receiver = ""
   message = ""

   try:
      opts, args = getopt.getopt(argv,"s:r:m:h","")
      
      if (len(opts)) == 0:
        usage()
        sys.exit()
   
   except getopt.GetoptError as e:
      print(e)
      usage()
      sys.exit()

   for opt, arg in opts:

      if opt == "-h":
         usage()
         sys.exit()

      elif opt in ("-s"):
         sender = arg

      elif opt in ("-r"):
         receiver = arg

      elif opt in ("-m"):
         message = arg

   msg = MIMEMultipart()
   msg.attach(MIMEText(message)) # attach message to MIME (msg)
 
   mailer = smtplib.SMTP(SERVER_ADDR, SERVER_PORT)

   print ("\n{$} Connecting..")
   mailer.starttls()
   mailer.login(USERNAME, PASSWORD)
   print ("{$} Server Connected!")

   spoofSender = sender + "/@gmail.com" # simple spoofing technique

   mailer.sendmail(spoofSender, receiver, msg.as_string())
   print ("{$} Sent!")
   mailer.close()

if __name__ == "__main__":
   main(sys.argv[1:])