import sys
import logging
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


def hello():
    print('Hello, World')



# ========================================================
#            Main 
# ========================================================    
if __name__ == '__main__':

    a = [1, 3]
    
    logging.debug("Sample Debug: %s" %a[0])

    print("a = {}".format(a))