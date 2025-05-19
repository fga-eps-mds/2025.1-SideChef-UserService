FROM python

WORKDIR /userservice

COPY ./requirements.txt /userservice/requirements.txt

RUN pip install --no-cache-dir -r /userservice/requirements.txt

COPY . /userservice

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]