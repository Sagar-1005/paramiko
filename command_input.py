import argparse
from backend_config import *

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--host',help='Enter host details',default=None)
    parser.add_argument('--operation',help='selct operation',default='running')
    parser.add_argument('--mode',help='Mode invoke_shell or exec_command',default='invoke_shell')
    args=parser.parse_args()
    if args.operation.lower()=='running' and args.mode.lower()=='invoke_shell':
        running_invoke_shell_config(args.host)
    elif args.operation.lower()=='running' and args.mode.lower()=='exec_command':
        running_exec_command(args.host)
    elif args.operation.lower()=='ssh_running' and args.mode.lower()=='exec_command':
        ssh_exec_command(args.host)
    

if __name__=='__main__': 
    main()