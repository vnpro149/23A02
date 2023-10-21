FROM ubuntu

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt app.py ./
RUN apt update && \
    apt install -y python3-pip && \
    pip3 install --no-cache-dir -r ./requirements.txt
EXPOSE 5000
CMD python3 ./app.py
