import datetime
import time
import getopt
import logging
import sys

class cwuArguments():
    def __init__(self, fullCmdArguments):
        self.today = datetime.date.today()
        self.dateformed = self.today.strftime("%m")+"_"+self.today.strftime("%d")+"_"+self.today.strftime("%Y")
        self.unixOptions = "ho:d:c:w:t:r:o:p:g:"
        self.db_basename = datetime.datetime.now().strftime("%m_%d_%Y/%H_%M_%S_%f")
        self.todays_date = datetime.datetime.now().strftime("%m_%d_%Y")
        self.todays_time = datetime.datetime.now().strftime("%H_%M_%S_%f")
        self.activerun = True
        self.sendemail = True
        self.test_this = True
        self.capwatch_date=self.todays_date
        self.gnuOptions = [
                           "help",
                           "activerun",
                           "testit"
                           ]
        # GET AND PARSE ARGUMENTS
        argumentList = fullCmdArguments[1:]
        try:
            arguments, values = getopt.getopt(argumentList, self.unixOptions, self.gnuOptions)
        except getopt.error as err:
            # output error, and return with an error code
            print (str(err))
            sys.exit(2)
        if(arguments.__len__() < 1):
                self.showHelp()
                sys.exit(0)
        else:
            for currentArgument, currentValue in arguments:
                if currentArgument in ("-d", "--cwdate"):
                    self.capwatch_date=currentValue
                elif currentArgument in ("--activerun"):
                    self.activerun = True
                elif currentArgument in ("--sendemail"):
                    self.sendemail = True
                elif currentArgument in ("--testit"):
                    self.test_this = True
                elif currentArgument in ("-p", "--path"):
                    self.path=currentValue
                elif currentArgument in ("-h", "--help"):
                    self.showHelp()
                    sys.exit(0)

    def showHelp(self):
        logging.info("--------------------------------------------------------------------")
        logging.info(" Civil Air Patrol WATCH utilities need an argument")
        logging.info(" ")
        logging.info(" capwatchutilities should not be used by themselves")
        logging.info("--------------------------------------------------------------------")
        logging.info(" Current DATE:        | "+self.dateformed)
        logging.info(" Option | argument    | Description                  | Current Value")
        logging.info("  -h    | --help      | Print this help              | ")
        logging.info("        | --cwdate    | Override CAPWATCH date       |["+self.capwatch_date+"] ")
        logging.info("        | --activerun | Actively run this command    |["+str(self.activerun)+"] ")
        logging.info("--------------------------------------------------------------------")
    
    def get_random_password(self):
        random_source = string.ascii_letters + string.digits
        # + string.punctuation
        # select 1 lowercase
        password = random.choice(string.ascii_lowercase)
        # select 1 uppercase
        password += random.choice(string.ascii_uppercase)
        # select 1 digit
        password += random.choice(string.digits)
        password += random.choice(string.digits)
        # select 1 special symbol
    
        # generate other characters
        for i in range(5):
            password += random.choice(random_source)
    
        #password += random.choice(string.punctuation)
        password_list = list(password)
        # shuffle all characters
        random.SystemRandom().shuffle(password_list)
        password = ''.join(password_list)
        return password

