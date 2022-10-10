FROM python:3.8-slim-buster
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5056
ENTRYPOINT [ "python" ]
CMD [ "login_service.py" ]