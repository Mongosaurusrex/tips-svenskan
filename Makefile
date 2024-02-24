start-db:
	@echo "Starting database..."
	@docker-compose up -d postgres

run-dev:
	@echo "Running dev environment..."
	@uvicorn server.main:app --host 0.0.0.0 --port 8000 --reload

run-tests:
	@echo "Running tests..."
	@pytest --cov=server server/tests/ 
