FROM python:3.12
WORKDIR app

COPY hi.py .

CMD ["python", "hi.py"]
