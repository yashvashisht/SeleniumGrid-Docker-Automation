# Simple Selenium Grid Facebook Test

This is a minimal Docker setup for running Facebook login tests using Selenium Grid.

## What it does
- Runs Selenium Grid with 1 Chrome browser
- Executes a Facebook login test script
- Allows viewing the live browser session

## Quick Start

### 1. Start the Grid
```bash
docker compose -f docker-compose-simple.yml up -d
```

### 2. Run the Facebook test
```bash
python fb_login_test.py
```

### 3. View the session
- **Grid UI**: http://localhost:4444/ui/#/sessions
- **Live Browser**: http://localhost:7900/?autoconnect=1&resize=scale&password=secret

### 4. Stop the Grid
```bash
docker compose -f docker-compose-simple.yml down
```

## Files
- `docker-compose-simple.yml` - Grid with 1 Chrome node
- `fb_login_test.py` - Facebook login test script

## Requirements
- Docker Desktop
- Python 3
- selenium package (`pip install selenium`)