import argparse
from backend_config import *

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--host',help='Enter host details',default=None)
    parser.add_argument('--operation',help='selct operation',default='running')
    args=parser.parse_args()
    if args.operation.lower()=='running':
        running_config(args.host)

if __name__=='__main__': 
    main()