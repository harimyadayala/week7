FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip install --no-cahche -dir -d falsk
EXPOSE 5000
CMD ["python3","app.py"]
