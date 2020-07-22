import platform, os
import subprocess
from subprocess import DEVNULL, STDOUT, check_call

# ping un hôte et renvoie true s'il est joignable
def ping(host):
    # Option for the number of packets as a function of
    param = '-n' if platform.system().lower()=='windows' else '-c'

    # Building the command. Ex: "ping -c 1 google.com"
    command = ['ping', param, '1', host]

    return subprocess.call(command, stdout=open(os.devnull, 'wb')) == 0 