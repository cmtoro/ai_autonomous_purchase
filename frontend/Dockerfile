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
RUN echo "sed -i 's|API_URL_PLACEHOLDER|'\$BACKEND_URL'|g' /usr/share/nginx/html/main*.js && nginx -g 'daemon off;'" > /entrypoint.sh
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
