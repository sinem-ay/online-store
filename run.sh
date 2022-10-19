export $(grep -v '^#' .env | xargs)

uvicorn api.product:router --reload