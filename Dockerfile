FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/app/contaazul


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY contaazul ./contaazul

CMD ["uvicorn", "contaazul.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
