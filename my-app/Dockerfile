FROM node:14-alpine as builder

WORKDIR /app

COPY package*.json ./
 
RUN npm install
# Install sweetalert2 package
RUN npm install --save sweetalert2

COPY . .

RUN npm run build

FROM nginx:stable-alpine

COPY --from=builder /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]