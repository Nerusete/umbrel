FROM python:3.12-alpine
WORKDIR /app
RUN pip install --no-cache-dir flask==3.1.2 werkzeug==3.1.3
COPY app.py /app/app.py
COPY templates /app/templates
RUN mkdir -p /app/data/uploads
EXPOSE 41100
CMD ["python","/app/app.py"]
