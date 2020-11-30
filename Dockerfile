FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt