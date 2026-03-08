# Stage 1: Build the Angular app
FROM node:alpine3.22 AS build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build --configuration=production

# Stage 2: Serve the app with Nginx
FROM nginx:stable-alpine
COPY --from=build /app/dist/purchase-app /usr/share/nginx/html

# Cloud Run sets $PORT (default 8080). Ensure nginx listens on it and inject Backend URL.
RUN cat > /entrypoint.sh <<'EOF'
#!/bin/sh

: "${PORT:=8080}"

# Replace backend URL placeholder in built JS bundles
sed -i "s|API_URL_PLACEHOLDER|${BACKEND_URL:-API_URL_PLACEHOLDER}|g" /usr/share/nginx/html/main*.js

# Ensure nginx listens on the port Cloud Run expects
sed -i "s/listen\s\+80;/listen ${PORT};/" /etc/nginx/conf.d/default.conf

exec nginx -g 'daemon off;'
EOF

RUN chmod +x /entrypoint.sh

EXPOSE 8080
ENTRYPOINT ["/entrypoint.sh"]
