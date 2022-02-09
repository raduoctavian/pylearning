import signal

#s = signal.valid_signals()
#print(s)

""" 
# Our signal handler
def signal_handler(signum, frame):  
    print("Signal Number:", signum, " Frame: ", frame)

signal_handler()
def my_custom_handler(signum, frame):
    print('I have encountered the signal KILL.')
    print('CTRL+C was pressed.  Do anything here before the process exits')
    
    
signal.signal(signal.SIGINT, my_custom_handler)
"""

def handler(signal_received, frame):
    # Handle any cleanup here
    print('SIGINT or CTRL-C detected. Exiting gracefully')
    print("Signal is:", signal_received, "and Frame is: ", frame)
    exit(0)

#if __name__ == '__main__':
    # Tell Python to run the handler() function when SIGINT is recieved
signal.signal(signal.SIGINT, handler)

print('Running. Press CTRL-C to exit.')
while True:
    #Do nothing and hog CPU forever until SIGINT received.
    pass