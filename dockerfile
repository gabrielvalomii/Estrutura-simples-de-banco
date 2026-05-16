FROM python:3.11-slim

LABEL maintainer="gabriel"
LABEL description="sistema simples de banco para inspirar quem esta iniciando na programação"

WORKDIR /app

COPY sistema.py .

CMD ["python", "sistema.py"]