import slowclap as sc
import time

# this is our detector function
def feed_func():
    try:
        feed = sc.MicrophoneFeed()
        detector = sc.AmplitudeDetector(feed, threshold=10000000) # threshold is changeable

        for clap in detector: # iteration over each incoming sample

            time.sleep(5) # protection against repeated tripping. changeable
            a = clap.time
            if a != 0:
                input_detector()
                break

    except OSError:
        feed_func()


# declare our purely logical functions
# this logic can always be changed to suit your needs

x = 1
def input_detector():
    global x
    x = -x
    stop_or_run(x)

def stop_or_run(x):
    if x == -1:
        print('run')
        run_func()
    else:
        print('stop')
        stop_func()



# subsequent functionality

def stop_func():
    #do anything...
    pass

def run_func():
    #do anything...
    pass

while True:
    feed_func()
