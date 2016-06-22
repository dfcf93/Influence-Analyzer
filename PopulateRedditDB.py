from multiprocessing import Process, Manager
import time
import itertools
import psycopg2
import csv
import json
import sys,getopt
class Config:
    def __init__(self, corpus, dbhost, dbname, dbuser, dbpassword):
        self.corpus = corpus
        self.dbhost = dbhost
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword
    def __str__(self):
        return self.corpus + ',' + self.dbhost + ',' + self.dbname + ',' + self.dbuser + ',' +  self.dbpassword
    def connprep(self):
	return 'dbname=' + self.dbname + ' user=' + self.dbuser + ' host=' + self.dbhost + ' password=' + self.dbpassword 
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

def TestDB(config):
    c = Config(config[0], config[1], config[2], config[3], config[4])
    print(c.connprep())
    conn = psycopg2.connect(c.connprep())
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute("SELECT * FROM TESTS;")
    print cur.query
    for record in cur:
        print record
def LoadIntoDB(threads, subreddit, config):

    manager = Manager()
    results = manager.list()
    work = manager.Queue(threads)

    # start for workers    
    pool = []
    for i in xrange(threads):
        p = Process(target=, args=(work, results))
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
if __name__ == '__main__':
   threads = ''
   subreddit = ''
   try:
      opts, args = getopt.getopt(sys.argv[1:],"hs:t:")
   except getopt.GetoptError:
      print 'PopulateDB.py -t <threads> -s <subredditid>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'PopulateDB.py -t <threads> -s <subredditid>'
         sys.exit()
      elif opt in ("-t", "--threads"):
         threads = arg
      elif opt in ("-s", "--subreddit"):
         subreddit = arg
   f = open('config.csv', 'r')
   config = csv.reader(f, delimiter=',').next()
   c = Config(config[0], config[1], config[2], config[3], config[4])
   i = 0
   with open(c.corpus, 'r') as f:
      for line in f:
         i+=1
         if i ==5:
            exit
         else:
            print(line)
  
