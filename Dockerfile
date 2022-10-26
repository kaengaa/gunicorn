FROM ubuntu:18.04
RUN apt-get update
RUN pip install gunicorn

ADD ./requirements.txt .
RUN pip install -r requirements.txt

RUN useradd -m user
RUN groupadd nginx
RUN usermod -a -G nginx user
RUN chmod 750 /home/user

ADD ./*.py /home/user/
WORKDIR /home/user

CMD gunicorn --bind 0.0.0.0:8000 wsgi:app
