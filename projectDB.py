
#importing modules
import sqlite3										#module to access the database	
from nltk.tokenize import word_tokenize				#module for tokenize the input
from nltk.corpus import stopwords					#module to stop unnessesary words
import warnings
import signal 										#To handle the keyboard interrupt		
import sys 
import logging    									#Logging Purpose
from config import Config                  			#To access config file
#---------------------------------------------------------------------------------------------------------------------
FORMAT='%(asctime)-15s Line:%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(filename="Demo.log",level=logging.DEBUG,format=FORMAT)    # Opens a new log files
#---------------------------------------------------------------------------------------------------------------------
#warning message
warnings.filterwarnings("ignore")
#---------------------------------------------------------------------------------------------------------------------
#Configuration file declaration
f=file("reg.cfg")											#Assigning the Config file
cfg=Config(f)  														

datapath=cfg.datapath
stud=sqlite3.connect(datapath)					#connecting to sqlite3
cursor=stud.cursor()
logging.info("Database is Created ")

#----------------------------------------------------------------------------------------------------------------------
#keywords
alldata=['alldetails','full','whole','all','ece','ECE','Ece'] #keywords Initialisation
great=['great','greater','>','above','more','plus','+','PLUS','exceedings']
less=['less','lesser','<','below']
equal=['equal','equals','exactly','=']
inequal=['inequal','unequal','!=']
highest=['highest','maximum','top','topper']
lowest=['lowest','minimum','least','loser']
MARKS=['MARKS','SCORED','GOT','got','ACQUIRED','OBTAINED',"SECURED","MARK",'mark']
var_case=[great,equal,inequal,less]
STATUS=["PASS","FAILED","FAIL","PASSED","CLEARED"]
titles=['NAME','ROLLNO','DEPARTMENT',MARKS,'STATUS']
#----------------------------------------------------------------------------------------------------------------------
#initial preparations
def query(user_input):
	try:

		stop_words =set(stopwords.words('english'))

		stop_words=list(stop_words)

		tokenized_input=word_tokenize(user_input)	#tokenizing the input 

		filetered_input = [w for w in tokenized_input if not w in stop_words]   #filtering only the necessary keywords
		if len(filetered_input)==0:
			print"Enter a valid question"


		mydata=cursor.fetchall()
		mydata=str(mydata)
		new=[]
		# print filetered_input
		for M in filetered_input:
			new.append(M)
	except(KeyboardInterrupt,SystemExit):
		signal.signal(signal.SIGINT,signal_handler())            #Warning for user	
		logging.warning("Program interrupted by user")
	logging.info("The user input is tokenized,filtered and stored in a list")
#------------------------------------------------------------------------------------------------------------------------
	upper_case=[]
	lower_case=[]
	for token in filetered_input:
		token=token.lower()
		lower_case.append(token)
		token=token.upper()
		upper_case.append(token)
	logging.info("The input stored in upper/lower cases")
#--------------------------------------------------------------------------------------------------------------------------------
#this block give us the pass/fail details and number of studens paased/failed in the class	
# try:
	for tokens in upper_case:
		STAT=0
		if tokens in STATUS:
			
			if tokens =="PASS" or tokens=="PASSED": 
				field='MARKS' 
				symbol='>='
				filetered_input=50
				# print "SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(field,symbol,filetered_input,field)
				cursor.execute("SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(field,symbol,filetered_input,field))
				for row in cursor.fetchall():
					print row
					STAT+=1
				print "No of students passed",STAT	
				return 0

			if tokens=="FAILED" or token=="FAIL":
				field='MARKS'
				symbol='<'	
				filetered_input=50	
				# print "SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(field,symbol,filetered_input,field)
				cursor.execute("SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(field,symbol,filetered_input,field))
				for row in cursor.fetchall():
					print row
					STAT+=1
				print "No of student failed",STAT
				return 0
# except Exception:
# 	print "Please enter the correct spelling for pass/fail"
		# logging.warning("Spelling is not correct")
	logging.info("Pass/fail status and count of pass/fail found")	
#---------------------------------------------------------------------------------------------------------------------------------
#this block works when user query based on the names
	try:
		for words in new:
			if words.isalpha():
				if not words in mydata:
					new.remove(words)
				cursor.execute ("SELECT * FROM STUDENT WHERE NAME ='%s' ORDER BY NAME ASC" %(new[0]))
				for row in cursor.fetchall():
					print row
					print ""
					return 0
	except Exception:
		print "Please enter the name as first charactor in caps"
		logging.warning("Name format not correct")
	logging.info("Query generated in basis of names")
#----------------------------------------------------------------------------------------------------------------------------------
#this block will return the highest/lowest scorer in the class
	try:	
		for list_elements in new:

			if list_elements in lowest:
				cursor.execute("SELECT * FROM STUDENT ORDER BY MARKS ASC LIMIT 1")
			elif list_elements in highest:
				cursor.execute("SELECT * FROM STUDENT ORDER BY MARKS DESC LIMIT 1")
			for row in cursor.fetchall():
				print row
			# return 0
	except Exception:
		print "Enter the proper keyword to find the highest/lowest marks f the class"
		logging.warning("keywords are not sufficient")
	logging.info("Highest/lowest marks of the class found")			
#----------------------------------------------------------------------------------------------------------------------------------
#this block bring the whole database when user want see all the details of the database
	try:
		for token in new:
			
			if token in alldata:
				cursor.execute("SELECT * FROM STUDENT ORDER BY NAME ASC")
				for row in cursor.fetchall():
					print row
	except Exception:
		print "If you want see the whole database Please try all keyword"
		logging.warning("Keywords are not sufficient")
	logging.info("Whole database printed")
#----------------------------------------------------------------------------------------------------------------------------------
#Case switching
# else:	
	for token in filetered_input:
		token=token.lower()
		lower_case.append(token)
		token=token.upper()
		upper_case.append(token)
#----------------------------------------------------------------------------------------------------------------------------------
#function to return the desired field name from database in query
		def fields():
			'''This function returns the field name according to the input '''
			try:
				for tokens in upper_case:
					if tokens in MARKS:
						field='MARKS'
						return field
						
					if tokens in titles:
						field=tokens	
				 		return field
			except Exception:
				print "Can't find the entered field"
				logging.warning("insufficient data")
			logging.info("fields are returned to the query")
		FIELDS=fields()
#----------------------------------------------------------------------------------------------------------------------------------
#funtion to assign the appropriate symbols			
		def symbols():
			'''this function will return the symbol according to the input'''		
			try:
				for different_case in var_case:				#assigning the appropriate symbols
					
					for different_case in lower_case:

						
						
						if different_case in great:
							symbol='>'
							return symbol
							break
						elif different_case in less:
							symbol='<'
							return symbol
							break
						elif different_case in equal:
							symbol='='
							return symbol
							break
						elif different_case in inequal:
							symbol='!='
							return symbol
							break				
			except Exception:
				print "Can't return the symbol"
				logging.warning("Insufficient data entered")
			logging.info("Symbols returned to the query")
		SYMBOLS=symbols()		
#------------------------------------------------------------------------------------------------------------------------------------
#this block will fetch the given data to the query
# try:						
		cursor.execute('''SELECT * FROM STUDENT''')
						
		mydata=cursor.fetchall()

		mydata=str(mydata)
		a_list=[]
		for datas in filetered_input:
			if datas not in mydata:
				required = filetered_input.index(datas)
				a_list.append(required)		
		for values in a_list[::-1]:
			filetered_input.pop(values)
# except Exception:
# 	print "Database don't contain any input keywords"
		logging.warning("Data not sufficient to process")
	logging.info("Data returned to the query")
#-------------------------------------------------------------------------------------------------------------------------------------	
#querying the database
#with single data

	if len(filetered_input)==1:
		try:
			Count=0
			
			# print "SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(FIELDS,SYMBOLS,filetered_input[0],FIELDS)
			a=cursor.execute("SELECT * FROM STUDENT WHERE %s %s '%s' ORDER BY %s ASC" %(FIELDS,SYMBOLS,filetered_input[0],FIELDS))
			for row in cursor.fetchall():
					print row
					Count+=1
			if Count<1:
				print"Enter a Valid Data"		
			print "count:",Count	
		except Exception:
			print "Given data not sufficient Please try again"
			logging.warning("Insufficient data to generate query")
		logging.info("Desired data printed")
#--------------------------------------------------------------------------------------------------------------------------------------
#querying between a range
	if len(filetered_input)>1:
		try:
			COUNT=0
			# print "SELECT * FROM STUDENT WHERE %s BETWEEN %s AND %s ORDER BY %s ASC" %(FIELDS,filetered_input[0],filetered_input[1],FIELDS)
			cursor.execute("SELECT * FROM STUDENT WHERE %s BETWEEN %s AND %s ORDER BY %s ASC" %(FIELDS,filetered_input[0],filetered_input[1],FIELDS))
			for row in cursor.fetchall():
					print row
					COUNT+=1
			if COUNT<1:
				print"Enter a Valid Data"		
			print"count:",COUNT	

		except Exception:
			print "Given data not sufficient Please try again"
			logging.warning("Insufficient data to generate query")
		logging.info("Desired data printed")
#--------------------------------------------------------------------------------------------------------------------------------------
#To handle Keyboard Interrupt
def signal_handler():							   										 				
	'''Exit the Program'''
	print "program terminated by user interrupt"
	sys.exit()									
#--------------------------------------------------------------------------------------------------------------------------------------
#main funtion
if __name__ == '__main__':
	while 1:
		print ''
		
		user=raw_input("Do you wish to initiate database query y/n:").strip()
		if user=='y'or user=='Y' or user=='YES' or user=='yes':
			try:
				user_input=raw_input("Please enter the question:").strip()
				if user_input:
					query(user_input)
				elif not user_input.isalnum():
					print "Enter the valid question"
				else:
					print "Enter the valid question"
			except(KeyboardInterrupt,SystemExit):
				print "Application interrupted by user"
				signal.signal(signal.SIGINT,signal_handler())            #Warning for user	

		elif user=='n'or user=='N'or user=='NO' or user=='no':
			sys.exit()
		else:
			print "please enter the valid option"