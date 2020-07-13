FROM python:3.8.3
RUN apt-get update; apt-get install sqlite3
RUN mkdir /opt/kabum
WORKDIR /opt/kabum
COPY requirements.txt .
COPY kabum/ ./kabum/
COPY entry.sh .
RUN pip install -r requirements.txt
RUN pip install gunicorn
ENTRYPOINT /opt/kabum/entry.sh

