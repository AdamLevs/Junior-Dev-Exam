FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY tracker.py .

CMD ["python", "-u", "tracker.py"]