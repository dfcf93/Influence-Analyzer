# Influence-Analyzer
A system that given a sub community identifies powerful users, language structure and paterns.

##Usage Guide
1. Create a VM or dev enviorment with a disk of at least 1 tb
2. Create a /datadrive folder that maps to free space or attached external disk.
3. Run  'make install' to setup the vm
4. Run 'make download' to dowload Reddit megafile'
5. (TODO) Create PSQL database and make sure the first VM can access the database and update the config.csv with your info.
6. (TODO) Run testDB.py to make sure the VM and DB are behaving as expected
7. (TODO) Find the redditId you want populate your PSQL DB with. This can be run multiple times for different subreddits.(example bellow is 20 threads and the Game of Thrones subreddit). If you arent sure what subreddit you want to explore I suggest using the google big query setup.
      '''Python
          PopulateRedditDB.py -threads 20 -subredditId t5_2rjz2 -config config.csv
      '''
8. (TODO) Once you have populated your db with what you want analyzed run the command bellow(using 20 threads and only using cascades with length > 3)
  '''Python
    AnalyzeDB.py -threads 20 -mincascade 3 -out outfile.txt -iterations 5 
9. Find a way to graph and have fun. 

Useful Notes
[Attaching a disk to Azure VM] (https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-classic-attach-disk/)
[Attaching a disk to PostgresDB] (https://cloud.google.com/solutions/setup-postgres-data-disk)
