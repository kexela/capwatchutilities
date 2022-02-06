import datetime
import time
import getopt
import logging
import sys
import os.path
import string
import random

class cwuArguments():
    def __init__(self, fullCmdArguments):
        logging.debug( "This python provides a basic python library ")
        logging.debug( " to help manage capwatch data for downstram ")
        logging.debug( " use.                                       ")
        logging.debug( "--------------------------------------------------------------------")
        logging.debug(" FEATURE LIST ")
        logging.debug(" Done?| Description                         ")
        logging.debug( "--------------------------------------------------------------------")
        logging.debug(" [YES]    | CAPWATCH DATABASE LOAD ")
        self.today               = datetime.date.today()
        self.dateformed          = self.today.strftime("%m")+"_"+self.today.strftime("%d")+"_"+self.today.strftime("%Y")
        self.db_basename         = datetime.datetime.now().strftime("%m_%d_%Y/%H_%M_%S_%f")
        self.todays_date         = datetime.datetime.now().strftime("%m_%d_%Y")
        self.todays_time         = datetime.datetime.now().strftime("%H_%M_%S_%f")
        self.activerun           = False
        self.sendemail           = True
        self.process_groups      = False
        self.process_requests    = False
        self.test_this           = True
        self.path                = ""
        self.password            = "myPassw0rd!"
        self.capnhqurl           = "api/get.me"
        self.baseurl             = "www.myurl.com"
        self.regionid            = "REG"
        self.topid               = 1
        self.wingid              = "ST"
        self.orgid               = 0
        self.capwatch_date       = self.todays_date
        self.capid               = 0
        self.basedir             = "."
        #    +cwuA.todays_date+".zip"
        unixOptions         = "ho:d:c:w:t:r:o:p:g:"
        gnuOptions = [
                           "help",
                           "path=",
                           "baseurl=",
                           "capnhqurl=",
                           "topid=",
                           "regionid=",
                           "wingid=",
                           "capid=",
                           "groups",
                           "procreqs",
                           "password=",
                           "activerun",
                           "wingemailsraw",
                           "orgid=",
                           "testit"
                           ]
        # GET AND PARSE ARGUMENTS
        argumentList = fullCmdArguments[1:]
        try:
            arguments, values = getopt.getopt(argumentList, unixOptions, gnuOptions)
        except getopt.error as err:
            # output error, and return with an error code
            print (str(err))
            sys.exit(2)
        if(arguments.__len__() < 1):
                self.showHelp()
                sys.exit(0)
        else:
            for currentArgument, currentValue in arguments:
                if(currentValue):
                    logging.info(" Setting "+currentArgument+" to "+currentValue)
                else:
                    logging.info(" Setting "+currentArgument+" to True")
                if currentArgument in ("-d", "--cwdate"):
                    self.capwatch_date=currentValue
                elif currentArgument in ("--activerun"):
                    self.activerun = True
                elif currentArgument in ("--procreqs"):
                    self.process_requests = True
                elif currentArgument in ("--groups"):
                    self.process_groups = True
                elif currentArgument in ("--topid"):
                    self.topid = currentValue
                elif currentArgument in ("--capid"):
                    self.capid = currentValue
                elif currentArgument in ("--password"):
                    self.password = currentValue
                elif currentArgument in ("--capnhqurl"):
                    self.capnhqurl = currentValue
                elif currentArgument in ("--wingid"):
                    self.wingid = currentValue
                elif currentArgument in ("--regionid"):
                    self.regionid = currentValue
                elif currentArgument in ("--baseurl"):
                    self.baseurl = currentValue
                elif currentArgument in ("--sendemail"):
                    self.sendemail = True
                elif currentArgument in ("--orgid"):
                    self.orgid = currentValue
                elif currentArgument in ("--testit"):
                    self.test_this = True
                elif currentArgument in ("-p", "--path"):
                    self.path=currentValue
                    self.zipdir = os.path.dirname(self.path+os.sep+self.basedir+os.sep+self.todays_date+os.sep)
                    logging.info(" Setting zipdir to "+self.zipdir+" [due to path setting]")
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
        logging.info("        | --activerun | Actively run this command    |["+str(self.activerun)+"] ")
        logging.info("        | --cwdate    | Override CAPWATCH date       |["+self.capwatch_date+"] ")
        logging.info("        | --capnhqurl | URL for full capwatch down   |["+str(self.capnhqurl)+"] ")
        logging.info("        | --procreqs  | Process Email Reqs Spreadsht |["+str(self.process_requests)+"] ")
        logging.info("        | --groups    | Process Group Memberships    |["+str(self.process_groups)+"] ")
        logging.info("        | --baseurl   | URL for full capwatch down   |["+str(self.baseurl)+"] ")
        logging.info("        | --orgid     | ID for organization wanted   |["+str(self.orgid)+"] ")
        logging.info("        | --regionid  | REGION ABBREVIATION          |["+str(self.regionid)+"] ")
        logging.info("        | --topid     | ORG top level ID             |["+str(self.topid)+"] ")
        logging.info("        | --capid     | CAP ID                       |["+str(self.capid)+"] ")
        logging.info("        | --wingid    | WING ABBREVIATION            |["+str(self.wingid)+"] ")
        logging.info("        | --password  | Account password             |["+str(self.password)+"] ")
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

