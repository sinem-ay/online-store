export $(grep -v '^#' .env | xargs)

uvicorn main:app --reload