FROM ubuntu:24.04

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
    nodejs \
    npm \
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

RUN curl -fsSL https://get.lando.dev/setup-lando.sh -o /tmp/setup-lando.sh \
    && chmod +x /tmp/setup-lando.sh \
    && /tmp/setup-lando.sh --version stable --no-setup --yes \
    && rm -f /tmp/setup-lando.sh

RUN mkdir -p /home/umbrel/umbrel/data/storage/lando-projects /root/.lando \
    && printf "proxy: 'OFF'\nbindAddress: '0.0.0.0'\nproxyBindAddress: '0.0.0.0'\n" > /root/.lando/config.yml \
    && echo false > /root/.lando/cache_report_errors 2>/dev/null || true

WORKDIR /home/umbrel/umbrel/data/storage/lando-projects

EXPOSE 7681

CMD ["ttyd", "--writable", "--port", "7681", "bash", "-lc", "echo 'Lando para Umbrel GO'; echo 'Proyectos: /home/umbrel/umbrel/data/storage/lando-projects'; echo; lando version; echo; exec bash"]
