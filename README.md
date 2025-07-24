# 🐍 Python + PostgreSQL with Docker

![Python](https://img.shields.io/badge/Python-3.10-blue)
![PostgreSQL](https://img.shields.io/badge/Postgres-Docker--Container-blue)
![Docker Compose](https://img.shields.io/badge/Docker-Docker--Compose-yellow)

This is a Python script (using Pandas) that registers users by uploading an Excel file and saves them into a PostgreSQL database running in a Docker container via Docker Compose.

---

## 🐳 Running PostgreSQL with Docker Compose

In your terminal:

1. Start the container:
```bash
docker-compose up
```

2. Check running containers:
```bash
docker ps
```

3. Find the container ID and inspect it:
```bash
docker inspect <container_id>
```

4. Copy the **IP address** shown under `NetworkSettings`.

5. Open PgAdmin4 in your browser:  
   [http://localhost:5050](http://localhost:5050)  
   - **User:** admin@email.com  
   - **Password:** password

6. Add a new server in PgAdmin using the IP address from step 4.

---

## 🐍 Running the Python Script

Once the container is up and database is configured, run:

```bash
python3 main.py
```

This will read the Excel file and insert the records into the PostgreSQL database.

---

## 🖼️ Screenshots

### Script Output

![main](https://user-images.githubusercontent.com/104561536/227084470-848eb0e8-9a3c-4e01-9140-1359c8753cef.png)

### PostgreSQL Container Running

![container_postgres](https://user-images.githubusercontent.com/104561536/227084746-86e5f50d-6a72-4dc6-9da3-47004809ca15.png)

---

## 🛠 Dependencies

- **pandas**
- **openpyxl**
- **psycopg2**
- **docker**
- **docker-compose**
- **PgAdmin4**

---

## 📄 License

MIT

---

_Last updated: 2025-07-23_
