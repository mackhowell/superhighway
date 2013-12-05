import shlex
import subprocess
import time

proc = subprocess.Popen(['tcpdump', '-w', 'myPackets.cap', '-i', 'eth0', 'ip'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
time.sleep(2)    # wait a few seconds
proc.terminate() # send SIGTERM instead of SIGKILL
proc.wait()      # avoid zombies
tcpdump_stderr = proc()[1]
print tcpdump_stderr
