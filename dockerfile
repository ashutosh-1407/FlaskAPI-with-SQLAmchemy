FROM python:3.6.12-slim
RUN mkdir /flaskapp
COPY . /flaskapp
WORKDIR /flaskapp
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python", "app/app.py"]