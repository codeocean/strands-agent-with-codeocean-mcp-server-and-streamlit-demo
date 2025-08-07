# hash:sha256:89c699af8d5eee4aae6e021a36c00e3e45c03954e222ed4f3077ea90ec781cc2
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:23.1.0-4-python3.10.12-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive
ARG CUSTOM_KEY
ARG CUSTOM_KEY_2
ARG CUSTOM_KEY_3

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    anthropic==0.61.0 \
    dotenv==0.9.9 \
    mcp==1.12.3 \
    strands-agents==1.3.0 \
    streamlit==1.48.0 \
    uv==0.8.5
