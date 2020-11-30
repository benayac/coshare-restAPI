FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]