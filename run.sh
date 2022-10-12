export $(grep -v '^#' .env | xargs)

uvicorn crud:app --reload