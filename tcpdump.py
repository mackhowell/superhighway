import shlex
import subprocess
import time

with open("tcpdumpSTDERR", "wb") as f_err: # close the file automatically
    proc = subprocess.Popen(shlex.split("tcpdump -w myPackets.cap -i eth0 ip"),
                            stderr=f_err)
time.sleep(2)    # wait a few seconds
proc.terminate() # send SIGTERM instead of SIGKILL
proc.wait()      # avoid zombies
print f_err
