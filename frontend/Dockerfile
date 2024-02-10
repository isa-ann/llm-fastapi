FROM node:16-alpine3.17

# set working directory
WORKDIR /frontend

# 
COPY package*.json ./

# Install project dependencies
RUN npm install

# add app
COPY . /frontend

# expose port
EXPOSE 3000

# start app
CMD ["npm", "start"]