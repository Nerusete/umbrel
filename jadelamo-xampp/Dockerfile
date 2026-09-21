FROM php:8.3-apache-bookworm

ENV TZ=Europe/Madrid

RUN apt-get update && apt-get install -y \
    libfreetype6-dev \
    libjpeg62-turbo-dev \
    libpng-dev \
    libwebp-dev \
    libzip-dev \
    libicu-dev \
    libonig-dev \
    unzip \
    git \
    curl \
    nano \
    && rm -rf /var/lib/apt/lists/*

RUN docker-php-ext-configure gd \
    --with-freetype \
    --with-jpeg \
    --with-webp

RUN docker-php-ext-install -j"$(nproc)" \
    mysqli \
    pdo_mysql \
    gd \
    zip \
    mbstring \
    intl \
    exif \
    opcache

RUN a2enmod rewrite headers expires

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf

RUN printf '%s\n' \
    'memory_limit=512M' \
    'upload_max_filesize=256M' \
    'post_max_size=256M' \
    'max_execution_time=300' \
    'max_input_time=300' \
    'date.timezone=Europe/Madrid' \
    > /usr/local/etc/php/conf.d/xampp.ini

RUN chown -R www-data:www-data /var/www/html

EXPOSE 80

CMD ["apache2-foreground"]
