FROM node:20-alpine AS build

WORKDIR /app

COPY web/package*.json ./

RUN npm ci

COPY web/ ./

RUN npm run build


FROM nginx:1.27-alpine

COPY --from=build /app/dist /usr/share/nginx/html

# arquivo de configuração custom
COPY infra/nginx/nginx.conf /etc/nginx/conf.d/default.conf
