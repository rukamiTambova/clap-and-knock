import slowclap as sc
import time

# this is our detector function
def feed_func():
    try:
        feed = sc.MicrophoneFeed()
        detector = sc.AmplitudeDetector(feed, threshold=10000000) # threshold is changeable

        for clap in detector: # iteration over each incoming sample

            time.sleep(1) # protection against repeated tripping. changeable
            a = clap.time
            if a != 0:
                input_detector()
                break

    except OSError:
        feed_func()


# declare our purely logical functions
# this logic can always be changed to suit your needs

x = 1
l = 0
def input_detector():
    global x
    x = -x
    stop_or_run(x)

def stop_or_run(x):
    if x == -1:
        print('STOP!')
        global l
        l = 1
        stop_func()
        return 'stop'
    else:
        print('RUN!')
        run_func()
        return 'run'



# subsequent functionality

def stop_func():
    return x

def run_func():
    #do anything
    pass

#while True:
    #feed_func()

def b_feed_func():
    while True:
        if l!=1:
            feed_func()
        else:
            #print('Exit')
            return 0
            break
#b_feed_func()