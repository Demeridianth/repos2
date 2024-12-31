FROM python:3.12.4 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app/app.py
COPY templates/index.html /app/templates/index.html
COPY static/styles.css /app/static/styles.css
EXPOSE 5000
CMD ["python3", "app.py"]

# docker build -t username/appname .   TO build in docker APP
# docker push username/appname    TO PUSH to DockerHub repository

# docker build -t appname .   TO build in docker APP
# docker tag image_name username/appname (repository name)

# docker push username/appname    TO PUSH to DockerHub repository

