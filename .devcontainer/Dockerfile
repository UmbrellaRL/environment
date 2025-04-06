FROM golang:1.24.2-bookworm

# Install required packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

ENV GOPATH=/go
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin
