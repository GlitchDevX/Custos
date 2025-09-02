# Stage 1: Generate Static Files
#FROM node:22-alpine AS builder
#
#COPY . .
#
#RUN pnpm ci
#
#RUN pnpm run generate


# Stage 2: Build Final Image
FROM nginx:stable-alpine

#COPY --from=builder .output/public /usr/share/nginx/html
COPY .output/public /usr/share/nginx/html

EXPOSE 80
