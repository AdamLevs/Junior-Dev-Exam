
# Junior-Dev-Exam

This project is a solution to a junior DevOps/Dev challenge.  
It includes a Python script that tracks Bitcoin price in **ILS (₪)** every minute, stores it in a PostgreSQL database, and prints insights with a trading recommendation.

---

## What the project does
- Fetches **BTC price in ILS** from [CoinGecko API](https://www.coingecko.com/)
- Stores every price point in a **PostgreSQL** database
- Calculates:
  - **Min price**
  - **Max price**
  - **Average price**
  - **Current price**
- Outputs a **recommendation**:
  - `Buy` if current price is at or below min
  - `Sell` if at or above max
  - `Hold` otherwise

  (Sample output:Value:
  396375 ₪ | Min: 395200 ₪ | Max: 398000 ₪ | Avg: 396800.00 ₪ | Recommendation: Hold)

---
## Stack & Technologies
- Language : Python
- Containers (2) : the app itself and the database
- DB : PostgreSQL
- Automation : Ansible
- API : CoinGecko (thats where i fetche the data)

---
## Project structure
```text
.
├── app/
│   ├── main.py              # the main app that run the enitre exam
│   ├── Dockerfile           # Builds the tracker container
│   └── requirements.txt     # Python dependencies
├── docker-compose.yml       # Defines services: PostgreSQL + Tracker
├── playbook.yml             # Ansible playbook to install Docker & run the app (bonus)
└── README.md                # This file
```
---

## How to run

### ⚙Prerequisites
- Docker is installed (that's the only assumption)
- Optional: Ansible (if using `playbook.yml`)

### Option 1: Run with Docker Compose
```bash
# the .env already inside so there is no need to set env

docker compose up --build
```

---
## Run with Ansible (Bonus)
well you tald me that i need to assume that docker already install, but i install the docker on Ansible, so even if it miss, it's still work, also i need to test that on my cloud testing machine.            
all you need to run (if Ansible installed):
```bash
ansible-playbook playbook.yml
```
---
## ENVIRONMENTS
```text
DB_HOST=localhost
DB_PORT=5432
DB_NAME=bitcoin
DB_USER=some_username
DB_PASS=some_password
```

