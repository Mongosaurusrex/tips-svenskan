include .env
export

.PHONY: help init-db migrate upgrade downgrade seed run up down
export PYTHONPATH := .

help:
	@echo "Available commands:"
	@echo "  make create-migration       - Generate a new Alembic migration (use NAME=message)"
	@echo "  make upgrade                - Apply migrations to the latest version"
	@echo "  make downgrade              - Revert to the previous migration (or set REV=xyz)"
	@echo "  make seed                   - Seed the database with sample leagues and teams"
	@echo "  make run                    - Run FastAPI app locally (with reload)"
	@echo "  make test                   - Run the test suite


create-migration:
ifndef NAME
	$(error Please provide a NAME, e.g., make migrate NAME=add_predictions_table)
endif
	alembic revision --autogenerate -m "$(NAME)"
	 
status:
	alembic current && alembic heads && alembic history 

upgrade:
	alembic upgrade head

downgrade:
ifndef REV
	alembic downgrade -1
else
	alembic downgrade $(REV)
endif

seed:
	python -m db.seed_data 

run:
	uvicorn main:app --reload

test: 
	pytest
