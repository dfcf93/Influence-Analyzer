rm size.txt
sudo -u postgres psql postgres -c "select count(id) from posts;" > size.txt &
