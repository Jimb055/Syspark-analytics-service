# AnalyticsService — SysPark

**AnalyticsService** is a microservice that provides system-wide usage statistics for the SysPark platform.  
Currently, it returns mock data, but it is designed to integrate with other services (UserService, BoardService, TaskService) in the future.

---

##  Features

- REST API built with **FastAPI**
- Exposes `GET /api/statistics` endpoint
- Returns mock statistics as a JSON response
- Containerized with **Docker**
- Ready for **CI/CD** and **AWS EC2 deployment**
- Clean, modular, and scalable architecture

---

##  Technologies Used

| Tool / Framework | Purpose                     |
|------------------|-----------------------------|
| Python 3.11+     | Main programming language   |
| FastAPI          | REST API framework          |
| Uvicorn          | ASGI server for FastAPI     |
| Docker           | Containerization            |
| GitHub Actions   | Continuous Integration (CI) |
| PostgreSQL       | Planned future integration  |
| AWS EC2          | Deployment environment      |

---

##  Project Structure

```
app/
├── api/                  # API routes
│   └── routes.py
├── models/               # (Optional) Pydantic schemas
│   └── statistics.py
├── services/             # Business logic
│   └── analytics_service.py
├── database.py           # DB connection (planned)
├── main.py               # FastAPI app entry point
```

---

##  Docker

> Build and run the service using Docker

```bash
# Build Docker image
docker build -t analytics-service .

# Run the container
docker run -p 8000:8000 analytics-service
```

---

##  API Reference

### `GET /api/statistics`

Returns mock aggregated metrics about SysPark platform usage.

#### Response Example:

```json
{
  "total_users": 123,
  "total_boards": 47,
  "pending_tasks": 320,
  "completed_tasks": 278
}
```

>  Note: These values are currently hardcoded. They will be dynamically calculated in future releases.

---

##  CI/CD (Planned)

GitHub Actions workflow will include:

- Code linting and unit testing
- Docker build & push
- Auto-deploy to AWS EC2 via SSH

---

##  Deployment

This service is deployed on **AWS EC2** and accessible at:

```bash
https://analytics.syspark.cloud/api/statistics
```

> Check DNS or IP mapping if not available yet.

---

##  Contributors

- [@Jimb055](https://github.com/Jimb055) — Lead Developer

---

##  License

MIT — feel free to use, modify, and distribute under the terms.