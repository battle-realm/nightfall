FROM python:3.10.5-alpine

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=app.py

COPY app /

ENTRYPOINT [ "flask"]
CMD [ "run", "--host", "0.0.0.0" ]
