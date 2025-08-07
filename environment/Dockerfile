# hash:sha256:c64a00fd16e2b21d2b1c77738e071e198b0afbf3fee3536f2748f82bc8bd9a55
ARG REGISTRY_HOST
FROM $REGISTRY_HOST/codeocean/mambaforge3:23.1.0-4-python3.10.12-ubuntu22.04

ARG DEBIAN_FRONTEND=noninteractive

ARG GIT_ASKPASS
ARG GIT_ACCESS_TOKEN
COPY git-askpass /

RUN pip3 install -U --no-cache-dir \
    anthropic \
    dotenv \
    mcp \
    strands-agents \
    streamlit \
    uv
