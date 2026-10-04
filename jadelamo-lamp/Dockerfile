FROM php:8.3-apache

RUN docker-php-ext-install mysqli pdo_mysql     && a2enmod rewrite

ENV TZ=Europe/Madrid

WORKDIR /var/www/html

COPY php.ini /usr/local/etc/php/conf.d/jadelamo.ini
