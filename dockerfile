FROM python:3.6.12-slim
WORKDIR /FlaskAPI
COPY . /FlaskAPI
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000

#CMD command launches the application when the container starts running.
CMD ["python", "app.py"]