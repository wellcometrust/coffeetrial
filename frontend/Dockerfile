# base image
FROM node:10.4.1-alpine

# set working directory
WORKDIR /rct-front

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /rct-front/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./package.json /rct-front/package.json
RUN npm install --silent
RUN npm install react-scripts -g --silent

# start app
CMD ["npm", "start"]
