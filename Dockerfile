FROM python:3.12.3-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN playwright install-deps
RUN playwright install chromium

EXPOSE 8501

CMD ["streamlit", "run", "main.py"]