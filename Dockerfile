FROM python:3

WORKDIR /usr/app



RUN pip install mysql-connector-python
COPY test.py ./
EXPOSE 8000
CMD ["python","test.py"]