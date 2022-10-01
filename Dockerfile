### 1. Get Alpine Linux
FROM alpine:latest

### 2. Label
LABEL maintainer="Dockerfile created by CL107 <https://github.com/CL107>"

### 3. Get dependencies
RUN apk update \
&& apk upgrade \
&& apk add python3 \
&& apk add py3-pip \
&& pip3 install python-dotenv

### 4. Copy server files
COPY ./server.py /rsa_pychat/server.py

### 5. Expose socket
EXPOSE 1234

### 6. Set working directory
WORKDIR /rsa_pychat

### 7. Start rsa_pychat server
CMD ["python3", "-u", "server.py"]
