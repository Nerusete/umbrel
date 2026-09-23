FROM ubuntu:24.04

ARG TARGETARCH

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Madrid
ENV LANDO_HOME=/root/.lando
ENV DOCKER_HOST=unix:///var/run/docker.sock

RUN apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    docker.io \
    docker-compose-v2 \
    ttyd \
    bash \
    openssh-client \
    jq \
    unzip \
    zip \
    rsync \
    nano \
    vim-tiny \
    procps \
    iproute2 \
    iputils-ping \
    dnsutils \
    && rm -rf /var/lib/apt/lists/*

RUN set -eux; \
    case "${TARGETARCH}" in \
      amd64) LANDO_ARCH="x64" ;; \
      arm64) LANDO_ARCH="arm64" ;; \
      *) echo "Unsupported architecture: ${TARGETARCH}" && exit 1 ;; \
    esac; \
    curl -fsSL "https://github.com/lando/core/releases/download/v3.26.9/lando-linux-${LANDO_ARCH}-v3.26.9" -o /usr/local/bin/lando; \
    chmod +x /usr/local/bin/lando; \
    lando version

RUN mkdir -p /home/umbrel/umbrel/data/storage/lando-projects /root/.lando /root/.lando/cache \
    && printf "proxy: 'OFF'\nbindAddress: '0.0.0.0'\nproxyBindAddress: '0.0.0.0'\n" > /root/.lando/config.yml \
    && echo false > /root/.lando/cache/report_errors

WORKDIR /home/umbrel/umbrel/data/storage/lando-projects

EXPOSE 7681

CMD ["ttyd", "--writable", "--port", "7681", "bash", "-lc", "echo '========================================'; echo ' LANDO PARA UMBREL GO'; echo '========================================'; echo; echo 'Proyectos: /home/umbrel/umbrel/data/storage/lando-projects'; echo; lando version; echo; echo 'Docker:'; docker version --format '{{.Server.Version}}' 2>/dev/null || true; echo; exec bash"]
