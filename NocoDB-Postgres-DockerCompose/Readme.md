This docker-compose file spins up a Postgres server in one container and a NocoDB "spreadsheet style" front end for it in another container.

NocoDB is an open source competitor to Airtable.

You can access the postgres database directly by connecting to localhost:5432 using "postgres" as the username and "postgress" as the password. You will need to have some sort of client to do this - you can't just visit that url in the browser. One example of a client is pgAdmin.

You access the Noco front end by visiting 'localhost:8080' in your browser.

**Run by using "docker-compose up -d"**
