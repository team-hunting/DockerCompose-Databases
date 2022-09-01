This docker-compose file spins up a Postgres server in one container and a Baserow "spreadsheet style" front end for it in another container.

Baserow is an open source competitor to Airtable.

You can access the postgres database directly by connecting to localhost:5432 using "postgres" as the username and "postgress" as the password. You will need to have some sort of client to do this - you can't just visit that url in the browser. One example of a client is pgAdmin.

You access the Baserow front end by visiting 'localhost' in your browser.

When you add tables using the Baserow interface, they end up as tables in your postgres database named "database_table_43" , "database_table_44", etc.


**Run by using "docker-compose up -d"**
