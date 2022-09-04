FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["uvicorn", "rest_server:app", "--reload", "--host", "0.0.0.0", "--port", "5000"]
