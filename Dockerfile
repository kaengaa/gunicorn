FROM python:3
RUN pip install flask && pip install gunicorn
ADD ./main.py /main.py
ADD ./wsgi.py /wsgi.py
EXPOSE 8000
CMD gunicorn --bind 0.0.0.0:8000 wsgi:app