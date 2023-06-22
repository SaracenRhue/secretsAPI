FROM python:3.11-slim

WORKDIR /home/user

COPY . .

RUN apt update && \
    apt install -y --no-install-recommends openssh-server sudo && \
    mkdir /var/run/sshd

RUN useradd -ms /bin/bash user && \
    echo "user:password" | chpasswd && \
    adduser user sudo

RUN pip install -r requirements.txt

WORKDIR /home/user/projects

ENV PORT=9000
EXPOSE 9000

ENV PORT=22
EXPOSE 22

VOLUME /home/user/projects

CMD /usr/sbin/sshd -D && \
    python run.py
