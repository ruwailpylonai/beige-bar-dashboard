# Beige Bar dashboard — isolated static preview (Pylon).
# Serves the self-contained index.html on Railway's $PORT. No dependencies.
FROM python:3.12-slim
WORKDIR /app
COPY . /app
ENV PORT=8080 PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["python", "server.py"]
