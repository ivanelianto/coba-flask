FROM python:3.6

WORKDIR /flask

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY . ./

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
