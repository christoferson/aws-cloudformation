# Application container. The MicroVM operating system itself comes from the
# Lambda managed base image (BaseImageArn in the template), not from this FROM.
FROM node:24-alpine

WORKDIR /app
COPY app.js .

EXPOSE 8080

# Lambda starts this during the build and snapshots the running process
CMD ["node", "app.js"]
