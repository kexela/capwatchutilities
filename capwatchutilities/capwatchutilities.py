import logging
import sys
from cwuArguments import cwuArguments as cwuA

def main():
    """
    """
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
    logging.info(f"Running capwatch utilities . . .")
    cwuA(sys.argv)
    logging.info("--------------------------------------------")
    logging.info("This python provides a basic python library ")
    logging.info(" to help manage capwatch data for downstram ")
    logging.info(" use.                                       ")
    logging.info("--------------------------------------------")
    sys.exit(0)

if __name__ == '__main__':
    main()

 