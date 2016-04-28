Process

1. Create 2 identical Ubuntu Servers and attach a [datadisk](https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-how-to-attach-disk/) to each one.
2. Configure [Postgres](https://cloud.google.com/solutions/setup-postgres-data-disk) on one and Set the datadirectory to your recently attached disk
3. Hit the ground

Copy (select * from posts where created > 1345335687 and created < 1348074030) To '/tmp/data1.csv' With CSV;

