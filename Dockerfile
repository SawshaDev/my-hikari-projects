FROM python:3.10-alpine

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt 

RUN apk add --no-cache linux-headers && apk --no-cache add gcc musl-dev && apk add libc-dev && apk add libffi-dev


COPY . . 

CMD [ "python3", "__main__.py" ]