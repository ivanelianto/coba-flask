FROM python:3.6

WORKDIR /flask

COPY . ./

RUN pip install -r requirements.txt

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
