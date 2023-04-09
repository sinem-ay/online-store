#!/bin/sh
export $(grep -v '^#' .env | xargs -d '\r')

uvicorn main:app --reload