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
COPY --from=build /app/dist/purchase-app/browser /usr/share/nginx/html

# Copiar script de entrada para reemplazar URL en tiempo de ejecución
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Ensure nginx listens on the port Cloud Run expects
RUN sed -i "s/listen\s\+80;/listen 8080;/" /etc/nginx/conf.d/default.conf

EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]
