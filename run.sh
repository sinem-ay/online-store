export $(grep -v '^#' .env | xargs)

uvicorn api.product:app --reload