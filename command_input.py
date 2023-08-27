import argparse
from backend_config import (
    config_compare,
    running_exec_command,
    running_invoke_shell_config,
    ssh_exec_command,
)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="Enter host details", default=None)
    parser.add_argument("--operation", help="selct operation", default="running")
    parser.add_argument(
        "--mode", help="Mode invoke_shell or exec_command", default="invoke_shell"
    )
    parser.add_argument("--diff", help="back_up_config")
    parser.add_argument("--comp_with")
    parser.add_argument("--comp_to")
    parser.add_argument("--html_normal")
    args = parser.parse_args()
    if args.diff == "backup":
        config_compare(args.comp_with, args.comp_to, args.html_normal)
    elif args.operation.lower() == "running" and args.mode.lower() == "invoke_shell":
        running_invoke_shell_config(args.host)
    elif args.operation.lower() == "running" and args.mode.lower() == "exec_command":
        running_exec_command(args.host)
    elif (
        args.operation.lower() == "ssh_running" and args.mode.lower() == "exec_command"
    ):
        ssh_exec_command(args.host)


if __name__ == "__main__":
    main()
