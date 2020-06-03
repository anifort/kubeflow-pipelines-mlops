FROM gcr.io/cloud-builders/kubectl

RUN apt update && \
    apt-get install -y python3 python-dev python3-dev build-essential \
    libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev python-pip && \
    apt install -y python3-pip && \
    pip3 install kfp==0.1.30

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD ./experiment_runner.py /app