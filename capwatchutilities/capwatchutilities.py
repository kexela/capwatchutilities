import logging
import sys
import os.path
from cwuArguments import cwuArguments
from cwucapnhq    import cwucapnhq
from cwuWings     import wing
from cwuO365      import office365
from cwujson      import cwujson

def main():
    """
    """
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.info( "--------------------------------------------------------------------")
    logging.info(f"Running capwatch utilities . . .")
    cwuA=cwuArguments(sys.argv)
    logging.info( "--------------------------------------------------------------------")
    logging.info(" - Loading Wing Organization Information from E-services (Password Required)")
    zipfile=os.path.join(cwuA.zipdir,cwuA.todays_date+".zip")
    if(os.path.exists(zipfile) == False):
        current_cw = cwucapnhq(basedir=cwuA.zipdir,
                            baseurl=cwuA.baseurl,
                            capnhqurl=cwuA.capnhqurl,
                            orgid=cwuA.orgid,
                            cw_dir=cwuA.basedir,
                            date=cwuA.todays_date,
                            output_filename=cwuA.todays_date+".zip")
        if(current_cw.getcw(username=cwuA.capid,password=cwuA.password) == False):
            logging.error("Unable to Load CAPWATCH DATABASE, please check password and connection")
            sys.exit(1)
    else:
        logging.info(" Processing Information for WING from: " + zipfile)
    logging.info( "--------------------------------------------------------------------")
    logging.info(" - Processing Wing Organization Information into Data Structures")
    theWing = wing(dateformed=cwuA.todays_date,
                   capid=cwuA.capid,
                   wing=cwuA.wingid,
                   org_id=cwuA.topid,
                   cap_region=cwuA.regionid,
                   wing_level_org_id=cwuA.orgid,
                   basedir=cwuA.basedir)
    logging.info(" Getting All User Account information")
    wingJson = cwujson(theWing.json_dir)
    json_tokens=wingJson.load_json_file(filename="O365.json")
    logging.info(" - FINISHED Processing Wing Organization Information")
    logging.info("--------------------------------------------------------------------")
    logging.info(" - IT Historical JSON")
    itJSON=wingJson.load_json_file(filename="it.json")
    ####### FORM {
    ####### FORM     "384814" : { "Active": true, "MSFT Account Created": true, "PasswordReset": false },
    ####### FORM     "000000" : { "Active": false, "MSFT Account Created": false, "PasswordReset": false },
    ####### FORM     "999999" : { "Active": false, "MSFT Account Created": false, "PasswordReset": false }
    ####### FORM }            
    logging.info("--------------------------------------------------------------------")
    logging.info(" Office 365 Administration Startup")
    office_inst=office365(client_id=json_tokens["client_id"],
                          client_secret=json_tokens["client_secret"],
                          tenant_id=json_tokens["tenant_id"],
                          emailDomain=json_tokens["email_domain"],
                          admin_client_id=json_tokens["admin_client_id"],
                          defaultLicense=json_tokens["defaultLicense"]
                          )
    if(cwuA.process_groups):
        logging.info( "--------------------------------------------------------------------")
        logging.info(" - Processing Groups")
        #scanbool=office_inst.loadgroups(printLogs=True)
        (groupBool)=office_inst.groupMaintenance(theWing,cwuA,itJSON,cwuA.activerun,printLogs=True)

    else:
        logging.info( "--------------------------------------------------------------------")
        logging.info(" - Diagnostic Checks on Office 365 organizations [FINISHED]")
        scanReturn=office_inst.scanCAPIDs(printLogs=True)
        logging.info(" - All accounts have an account issued with Name, RANK and CAPID - [TESTING]")
        (acctReturn,itJSONret)=office_inst.scanUNITs(theWing,cwuA,itJSON,cwuA.activerun,printLogs=True)
        logging.info(" - [NOT FINISHED] - All accounts have a backup email (otherMail) assigned ")
        logging.info(" - [NOT FINISHED] - Check Squadron CC all have aliases assigned ")
        # History for each CAPID can be references as itJSON["NNNNNN"] where N is the local capid
        wingJson.save_json_file(itJSONret,"it."+cwuA.todays_date+".json",print_logs=True)
        logging.info("-----------------------------------")


    sys.exit(0)

if __name__ == '__main__':
    main()