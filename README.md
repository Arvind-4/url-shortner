# Url Shortner

A simple URL shortener built using Django and PostgreSQL.

## Features

- Shorten URLs
- Redirect to original URLs
- Get top visited domains
- Get metrics

## Local Setup (Docker)

1. Clone the repository
2. Run `docker compose up --build` to start the application

## Local Setup

1. Clone the repo
2. copy the contents of `.env.docker` to `.env`.
3. Install the requirements from `requirements.txt`.
4. Run the dev server by the command `python manage.py runserver`

## Try the api!

```bash
curl --location 'https://awesomeurlshortner.vercel.app/shorten/' \
--header 'Content-Type: application/json' \
--data '{
    "url": "facebook.com"
}'
```

## Url Routes:

- **`shorten/` (POST)**: Takes a URL in the request body, validates it, creates or retrieves a shortened URL, and returns the shortened URL in a JSON response.
- **`metrics/` (GET)**: Returns a JSON response with the top 3 most common domains from all shortened URLs in the database.
- **`<str:path>/` (GET)**: Takes a shortcode from the URL path, looks it up in the database, and redirects to the original URL associated with that shortcode.
