FROM node:20-alpine

RUN apk add --no-cache python3 make g++

WORKDIR /app

COPY package.json ./
RUN npm install --omit=dev

COPY index.js ./

ENV NODE_ENV=production
ENV PORT=3789
EXPOSE 3789

# 数据卷挂到 /app/data
VOLUME ["/app/data"]

CMD ["node", "index.js"]
