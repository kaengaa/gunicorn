FROM python:3.9
RUN  pip install --upgrade pip && pip install flask gunicorn pymysql cryptography
ADD *.py /
EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app