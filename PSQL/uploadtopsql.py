
from multiprocessing import Process, Manager
import time
import itertools
import psycopg2
import csv
import json
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

def dbWrite(inQueue, cfaur):
    while True:
        item = inQueue.get()
        lineNo, line = item
        if line == None:
            return
        j = json.loads(line)
        if j['is_self'] != None:
            print 'ttt'#try:
             #   cur.execute("INSERT INTO POSTS(postid, subreddit, subredditid, author, url, urldomain, media, title, score, downvotes, upvotes, comments, created) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)", (j['id'], j['subreddit'], j['subreddit_id'], j['author'], j['url'], j['domain'], j['media'], j['title'], j['score'], j['downs'], j['ups'], j['num_comments'], j['created_utc']))
            #except:
             #   print "something crashed"
              #  print cur.query
               # print i
                
if __name__ == '__main__':
    
    workers = 1  
    
    manager = Manager()
    results = manager.list()
    work = manager.Queue(workers)

    pool = []
    for i in xrange(workers):
        p = Process(target=dbWrite, args(work,cur))
        p.start()
        pool.append(p)
  
    f = open('config.csv', 'r') as f:
    config = csv.reader(f, delimiter=',').next()
    c = Config(config[0], config[1], config[2], config[3], config[4])
    conn = psycopg2.connect(c.connprep())
    conn.autocommit = True
    cur = conn.cursor()
    i = 0

  
    while i < 1000:    
        with open(c.corpus,'r') as corpus:
            iters = itertools.chain(corpus, (None,)*workers)
            for line in enumerate(iters):
                work.put(line)
                i++
    cur.close()
    conn.close()
    print i
