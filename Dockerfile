### 1. Get Linux
FROM alpine:latest

### 2. Label
LABEL maintainer="Dockerfile created by CL107 <https://github.com/CL107>"

### 3. Get dependencies
RUN apk update \
&& apk upgrade \
&& apk add python3

### 4. Copy requirements.txt

COPY ./server.py /rsa_pychat/server.py

### 5. Expose web ui port
EXPOSE 1234

### 6. Set working directory
WORKDIR /rsa_pychat

### 7. Start crafty
CMD ["python3", "server.py"]
