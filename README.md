# python-postgres-docker
This is a Python program (using Pandas) that register users through uploading an Excel file and save them into Postgres Database. The Database will be a Docker Container setup through Docker Compose.

## To run Docker Container Postgres through Docker Compose

On the terminal:

1. Execute $docker-compose up
2. Execute $docker ps to check the Postgres ID
3. Execute $docker inspect <ID of postgres container>
4. Copy the "IP address".
5. Open the PgAdmin4: http://localhost:5050
6. user= admin@email.com & password= password
7. Set up new server using the same IP from the step 4.


## Executing the program

On the terminal, type the command python3 main.py

![main](https://user-images.githubusercontent.com/104561536/227084470-848eb0e8-9a3c-4e01-9140-1359c8753cef.png)


## Docker  Container Postgres

![container_postgres](https://user-images.githubusercontent.com/104561536/227084746-86e5f50d-6a72-4dc6-9da3-47004809ca15.png)

