FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

# Install AWS CLI via pip (no apt-get needed)
RUN pip install awscli
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]
