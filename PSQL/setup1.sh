sudo add-apt-repository ppa:webupd8team/java && apt-get update
sudo apt-get install libfftw3-bin libfftw3-dev lsscsi vim curl git python-software-properties zsh oracle-java8-installer oracle-java8-set-default erlang erlang-doc geomview pip libpq-dev python-dev
sudo apt-get install -y libhttp-parser2.1 libicu52 libpq
pip install setuptools 
pip install psycopg2
sudo wget -P  /datadrive  http://reddit-data.s3.amazonaws.com/RS_full_corpus.bz2 
sudo bunzip2 /datadrive/RS_full_corpus.bz2
