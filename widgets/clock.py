import nsq
import time


if __name__ == '__main__':

    #Reader instantiation
    w = nsq.Writer(['http://127.0.0.1:4151'], name="clock_widget")
    w.pub('test', time.time())
    nsq.run()