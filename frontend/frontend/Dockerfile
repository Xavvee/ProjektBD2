# frontend/Dockerfile
FROM node:16.15.1

RUN mkdir /app
WORKDIR /app

COPY package.json /app/
RUN npm install
RUN npm install -g @angular/cli

COPY . /app/
