FROM mongo:3.4

RUN apt-get update \
  && apt-get install -y python3 python3-pip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

RUN pip3 install pytest pytest-cov

CMD ["/bin/bash"]
