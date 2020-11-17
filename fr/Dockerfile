FROM node:12.18.3

WORKDIR /app

ENV PATH /app/node_modules/.bin$PATH

COPY package.json /app/package.json
RUN npm install -g @vue/cli
RUN npm install -g @vue/cli-service-global
RUN npm install --save-dev eslint@latest
#RUN npm install --save-dev eslint@
RUN npm install -g @vue/cli@latest
RUN npm install



COPY . .
EXPOSE 8080
# start app
CMD npm run serve
#CMD ["npm", "run", "serve"]
#--host 0.0.0.0