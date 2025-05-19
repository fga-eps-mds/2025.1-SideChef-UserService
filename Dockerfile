FROM python:alpine

WORKDIR /userservice

COPY ./requirements.txt /userservice/requirements.txt

RUN pip install --no-cache-dir -r /userservice/requirements.txt

COPY . /userservice

COPY start.sh /start.sh

RUN chmod +x /start.sh

CMD ["/start.sh"]