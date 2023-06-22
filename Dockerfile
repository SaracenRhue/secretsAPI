FROM python:3.11-slim

WORKDIR /home/app

COPY . .

RUN apt update && \
    apt install -y --no-install-recommends openssh-server && \
    echo "root:secrets" | chpasswd && \
    mkdir /var/run/sshd

RUN pip install -r requirements.txt

ENV PORT=9000
EXPOSE 9000

ENV PORT=22
EXPOSE 22

VOLUME /home/app/projects

CMD /usr/sbin/sshd -D && \
    python run.py
