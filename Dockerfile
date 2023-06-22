FROM python:3.11-slim

WORKDIR /home/app

COPY . .

RUN pip install -r requirements.txt

ENV PORT=9000
EXPOSE 9000

VOLUME /home/app/projects

CMD python run.py
