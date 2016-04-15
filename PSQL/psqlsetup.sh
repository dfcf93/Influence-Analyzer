sudo apt-get update
sudo apt-get -y install postgresql postgresql-clien postgresql-contrib lsscsi
sudo -s
sudo -u postgres psql postgres
\password postgres
Create EXTENSION adminpack;
\q 
sudo nano ../../etc/postgresql/9.4/main/pg_hba.conf
sudo nano ../../etc/postgresql/9.4/main/postgresql.con
sudo service postgresql restart
sudo fdisk  /dev/sdc/
sudo mkfs -t ext4 /dev/sdc1 #make the file system on new partition 
sudo mkdir /media/postgres-data
sudo mount /dev/sdc1 /media/postgres-data
sudo -i blkid #use this to get the UUID
