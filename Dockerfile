FROM python:3.8-slim-buster
MAINTAINER Jainaveen
COPY ./login_service ./login_service
WORKDIR ./login_service
RUN pip install -r requirements.txt
EXPOSE 5056
CMD python login_service.py