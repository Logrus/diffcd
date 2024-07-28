FROM ubuntu:jammy

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
    git \
    git-lfs \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    ffmpeg \
    libsm6 \
    libxext6 \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN python3 -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
