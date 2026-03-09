# Stage 1: Build the Angular app
FROM node:22-alpine AS build
WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build -- --configuration=production

# Stage 2: Serve with Nginx
FROM nginx:alpine

# Angular 17+ outputs to dist/<project>/browser
COPY --from=build /app/dist/purchase-app /usr/share/nginx/html

# Cloud Run sets $PORT (default 8080). Ensure nginx listens on it and inject Backend URL.
RUN sed -i "s|API_URL_PLACEHOLDER|${BACKEND_URL:-API_URL_PLACEHOLDER}|g" /usr/share/nginx/html/*.js

# Ensure nginx listens on the port Cloud Run expects
RUN sed -i "s/listen\s\+80;/listen 8080;/" /etc/nginx/conf.d/default.conf

EXPOSE 8080
CMD ["nginx", "-g", "daemon off;"]
