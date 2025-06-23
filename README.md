# Choreo Sample Python REST API

This is a sample Python REST API built with FastAPI for deployment on Choreo.

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## API Endpoints

- `GET /`: Welcome message
- `GET /items`: List all items
- `POST /items`: Create a new item
- `GET /items/{item_id}`: Get a specific item by ID

## Docker Build

```bash
docker build -t choreo-sample-api .
docker run -p 8080:8080 choreo-sample-api
```

## Deploying to Choreo

1. Push this code to a GitHub repository
2. Log in to Choreo Console (https://console.choreo.dev/)
3. Create a new service component
4. Select "Container" as the component type
5. Connect your GitHub repository
6. Deploy the service

The API will be automatically built and deployed on Choreo platform.
