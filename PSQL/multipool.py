from multiprocessing import Process, Manager
import time
import itertools 

def do_work(in_queue, out_list):
    while True:
        item = in_queue.get()
        line_no, line = item

        # exit signal 
        if line == None:
            return

        # fake work
        time.sleep(.5)
        result = (line_no, line)

        out_list.append(result)


if __name__ == "__main__":
    num_workers = 4

    manager = Manager()
    results = manager.list()
    work = manager.Queue(num_workers)

    # start for workers    
    pool = []
    for i in xrange(num_workers):
        p = Process(target=do_work, args=(work, results))
        p.start()
        pool.append(p)

    # produce data
    with open("source.txt") as f:
        iters = itertools.chain(f, (None,)*num_workers)
        for num_and_line in enumerate(iters):
            work.put(num_and_line)

    for p in pool:
        p.join()

    # get the results
    # example:  [(1, "foo"), (10, "bar"), (0, "start")]
    print sorted(results)
