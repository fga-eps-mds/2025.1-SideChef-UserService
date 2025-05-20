FROM python:3.13-slim

WORKDIR /userservice

COPY ./requirements.txt /userservice/requirements.txt

RUN pip install --no-cache-dir -r /userservice/requirements.txt

COPY . /userservice

CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]