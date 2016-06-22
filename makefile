dothis:
	echo "this"
dothat:
	@echo "that"
install:
	@echo "this is where installation would happen"
	@sudo add-apt-repository ppa:webupd8team/java
	@sudo apt-get upgrade
	@sudo apt-get update
	@sudo apt-get install oracle-java8-installer oracle-java8-set-default lsscsi xclip
	@sudo apt-get install vim curl git python-software-properties python-pip python-dev
	@sudo apt-get install libpq-dev
	@sudo pip install setuptools
	@sudo pip install psycopg2
download:
	@sudo wget -p /datadrive http://reddit-data.s3.amazonaws.com/RS_full_corpus.bz2
	@sudo bunzip2 /datadrive/RS_full_corpus.bz2	
update:
	@sudo apt-get update
	@sudo apt-get upgrade
	@git pull

