FROM node:lts

WORKDIR /app

COPY . .
RUN npm install

EXPOSE 8080

CMD ["npm", "run", "start", "--", "--host", "0.0.0.0" ]