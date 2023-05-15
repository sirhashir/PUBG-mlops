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
# configuration options (-g "daemon off;"), which prevents the 
# server from running as a background daemon and allows the container to remain active.