FROM python:3.12.4 
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py /app/app.py
COPY templates/index.html /app/templates/index.html
EXPOSE 5000
CMD ["python3", "app.py"]