#!/bin/sh

# Reemplazar API_URL_PLACEHOLDER con la URL del backend en tiempo de ejecución
BACKEND_URL=${BACKEND_URL:-API_URL_PLACEHOLDER}

# Reemplazar en todos los archivos JS compilados
find /usr/share/nginx/html -type f -name "*.js" -exec sed -i "s|API_URL_PLACEHOLDER|$BACKEND_URL|g" {} +

# Opcional: también en archivos HTML si es necesario
find /usr/share/nginx/html -type f -name "*.html" -exec sed -i "s|API_URL_PLACEHOLDER|$BACKEND_URL|g" {} +

# Iniciar nginx
exec nginx -g "daemon off;"
