import time
import sys


def count_down(secs):
    sleep_per = 5
    for i in range(int(secs / sleep_per)):
        log_it("Remaining:{} secs".format(secs - i * sleep_per))
        time.sleep(sleep_per)


def log_it(msg):
    sys.stdout.write(msg)
    sys.stdout.write("\n")
    sys.stdout.flush()


log_it("Running required actions...")
count_down(10)
log_it("Finished.")
