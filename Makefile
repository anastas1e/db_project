run-db:
	docker run --name mydb -p 5433:5433 -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -v ${PWD}/db_data:/var/lib/postgresql/data -d postgres