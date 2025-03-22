FROM python:3.13.1-slim
ARG SOLC_VERSION="0.8.0"
RUN apt update && apt install --yes openjdk-17-jdk-headless && apt install --yes git build-essential curl
RUN pip3 install solc-select && pip3 install certora-cli && pip3 install halmos 
RUN solc-select install ${SOLC_VERSION} && solc-select use ${SOLC_VERSION}
RUN mkdir -p /project
WORKDIR /project
ENTRYPOINT ["bash"]
