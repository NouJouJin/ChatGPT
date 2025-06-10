# ChatGPT

Simple Flask web app to manage farm product reservations.

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
2. Activate it:
   ```bash
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Initialize the database with sample data:
   ```bash
   export FLASK_APP=app
   flask init-db
   ```
5. Run the application:
   ```bash
   flask run
   ```
6. Open `http://localhost:5000` in your browser.

## Running Tests

Install `pytest` and run the tests from the repository root:

```bash
pip install pytest
pytest
```
