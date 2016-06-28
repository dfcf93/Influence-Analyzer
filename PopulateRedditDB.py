from multiprocessing import Process, Manager
import time
import itertools 
import sys,getopt,json, csv
class Config:
    def __init__(self, corpus, dbhost, dbname, dbuser, dbpassword, threads, subredditid):
        self.corpus = corpus
        self.dbhost = dbhost
        self.dbname = dbname
        self.dbuser = dbuser
        self.dbpassword = dbpassword
        self.threads = threads
        self.subredditid = subredditid
    def __str__(self):
        return self.corpus + ',' + self.dbhost + ',' + self.dbname + ',' + self.dbuser + ',' +  self.dbpassword + "," + self.threads + ',' + self.subredditid
    def connprep(self):
	    return 'dbname=' + self.dbname + ' user=' + self.dbuser + ' host=' + self.dbhost + ' password=' + self.dbpassword 
class Post:
    def __init__(self,post):
        #do work
        return
    def __str__(self):
        return "self"
    def ReturnInsert(self):
        return "INSERT into Posts ()"
def insert(config, line):
    p = Post(line)
    if p.subredditid == config.subredditid:
        p.ReturnInsert    
        conn = psycopg2.connect(c.connprep())
        cursor = conn.cursor()
        cursor.execute(p.ReturnInsert)
        cursor.close()
        connection.commit()
    else:
        return
def LoadIntoDB(config):
    pool = []
    manager = Manager()
    work = manager.Queue(config.threads)
    for i in xrange(config.threads):
        p = Process(target=insert, args=(config, line))
        p.start()
        pool.append(p)
    with open(config.corpus) as f:
        iters = itertools.chain(f, (None,)*config.threads)
        for line in enumerate(iters):
            work.put(line)
    for p in pool:
        p.join()
def GetConfig(filename,threads,subredditid):
   config = list(open(filename))[0].split(',')
   return Config(config[0], config[1], config[2], config[3], config[4], threads, subredditid)
if __name__ == '__main__':
   threads = ''
   subredditid = ''
   config = ''
   try:
      opts, args = getopt.getopt(sys.argv[1:],"t:s:c:h")
   except getopt.GetoptError:
      print('PopulateDB.py -t <threads> -s <subredditid> -c <config>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('PopulateDB.py -t <threads> -s <subredditid> -c <config>')
         sys.exit()
      elif opt in ("-t"):
         threads = arg
      elif opt in ("-s"):
         subredditid = arg
      elif opt in ("-c"):
         config = arg
   LoadIntoDB(GetConfig(config, threads,subredditid)) 