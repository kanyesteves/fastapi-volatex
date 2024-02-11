FROM python:slim-bookworm

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "controller:app", "--host", "0.0.0.0", "--port", "8000"]
