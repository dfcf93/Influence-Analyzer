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
if __name__ == '__main__':
    f = open('config.csv', 'r')
    config = csv.reader(f, delimiter=',').next()
    c = Config(config[0], config[1], config[2], config[3], config[4])
    conn = psycopg2.connect(c.connprep())
    conn.autocommit = True
    print(conn.str)
    cur = conn.cursor()
    cur.execute("SELECT * FROM TESTS;")
    print cur.query
    for record in cur:
        print record
