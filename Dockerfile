
FROM python:3.8

WORKDIR /app

RUN pip install -r requirements.txt

COPY script.py /app/

CMD ["python", "script.py"]
