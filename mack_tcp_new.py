import subprocess

MAX_PACKETS = 50
counter = 0

class TCPListener:
    """MAK TCPListener"""
    def __init__(self, max_packets=MAX_PACKETS, callback=None):
        self.callback = callback
        self.max_packets = max_packets
        self.proc = None  # temporary

    def run(self):
        self.runOutput(callback=self.callback)
        print self.runOutput(callback=self.callback)
        #self.proc.terminate()

    def runOutput(self, callback):
        args = ['sudo', 'tcpdump', '-i', 'eth0', '-c', str(self.max_packets)]
        self.proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        # print "self.proc.poll() is: ", self.proc.poll()
        while self.proc.poll() is None:  # hopefully one day this will be fixed, this is always None
            output = self.proc.stdout.readlines()
            for thing in output:
                callback(thing)


def my_callback(arg):
    global counter
    counter += 1
    # print counter


def main():
    listener = TCPListener(max_packets=MAX_PACKETS, callback=my_callback)
    listener.run()

if __name__ == '__main__':
    main()
