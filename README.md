# AnalyticsService — SysPark

**AnalyticsService** is a microservice that provides system-wide usage statistics for the SysPark platform.  
This includes aggregated data such as the total number of users, boards, and tasks completed or pending.

---

##  Features

- REST API built with **FastAPI**
- Exposes `GET /api/statistics` for system-wide analytics
- Ready for **Docker**, **CI/CD**, and **AWS EC2 deployment**
- Clean and modular architecture

---
##  Technologies Used

| Tool / Framework | Purpose                     |
|------------------|-----------------------------|
| Python 3.11+     | Main programming language   |
| FastAPI          | REST API framework          |
| Uvicorn          | ASGI server for FastAPI     |
| Docker           | Containerization            |
| GitHub Actions   | Continuous Integration (CI) |
| PostgreSQL       | (planned) data source       |
| AWS EC2          | (planned) deployment target |

---

##  Project Structure

```
app/
├── api/                # API routes
│   └── routes.py
├── models/             # Pydantic schemas
│   └── statistics.py
├── services/           # Business logic
│   └── analytics_service.py
├── main.py             # FastAPI app entry point
```

---

##  Docker

> Build and run the service using Docker (once configured)

```bash
# Build Docker image
docker build -t analytics-service .

# Run the container
docker run -p 8000:8000 analytics-service
```

---

##  API Reference

### `GET /api/statistics`

Returns aggregated metrics about SysPark platform usage.

**Sample Response:**
```json
{
  "total_users": 123,
  "total_boards": 47,
  "pending_tasks": 320,
  "completed_tasks": 278
}
```

---

##  CI/CD (Planned)

- GitHub Actions workflow for:
  - Linting / testing
  - Build & Docker push
  - Deploy to AWS EC2

---

##  Deployment (Planned)

This service will be deployed to **AWS EC2**, accessible via:

```bash
https://analytics.syspark.cloud/api/statistics
```

---

##  Contributors

- [@Jimb055](https://github.com/Jimb055) — Lead Developer

---

##  License

MIT — feel free to use, modify and distribute under the terms.
