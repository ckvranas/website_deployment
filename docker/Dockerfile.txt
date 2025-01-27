FROM python:3.10-alpine   
WORKDIR /app
COPY requirements.txt /app/
COPY src-python/app.py /app/
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 4000
CMD ["python3", "app.py"]