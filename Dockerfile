FROM python:3.8

RUN apt-get update && apt-get upgrade -y && \
    apt install -y netcat-openbsd

RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["./deploy-api.sh"]