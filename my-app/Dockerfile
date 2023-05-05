FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install

COPY my-app/ .

EXPOSE 8080

CMD [ "npm", "start" ]
