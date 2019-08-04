FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install apscheduler
RUN pip install pymongo
RUN pip install -r requirements.txt
