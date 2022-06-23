FROM python:3.9.13-slim-buster

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY app /
ENTRYPOINT [ "python", "/app.py" ]
