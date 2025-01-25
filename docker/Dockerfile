FROM ubuntu:20.04
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get install -y \
    python3 \
    python3-pip \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*    
WORKDIR /app
COPY requirements.txt /app/
COPY src-python/app.py /app/
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 000
CMD ["python3", "app.py"]