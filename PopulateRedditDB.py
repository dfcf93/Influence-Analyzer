from multiprocessing import Process, Manager
import time
import itertools 
import psycopg2
import sys,getopt,json, csv
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
def buildquery(line):
    return line
def insert(config, line):
    conn = psycopg2.connect(c.connprep())
    cursor = conn.cursor()
    cursor.execute(buildquery(line))
    cursor.close()
    connection.commit()
def LoadIntoDB(threads, subreddit, config):
    pool = []
    manager = Manager()
    work = manager.Queue(threads)
    for i in xrange(threads):
        p = Process(target=insert, args=(config, line))
        p.start()
        pool.append(p)
    with open(c.corpus, 'r') as f:
        for line in f:
           iters = itertools.chain(f, (None,)*num_workers)
           for num_and_line in enumerate(iters):
            work.put(num_and_line)
    # produce data
    with open("source.txt") as f:
        iters = itertools.chain(f, (None,)*num_workers)
        for line in enumerate(iters):
            work.put(line)
    for p in pool:
        p.join()
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
  
