FROM python:3.8

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app.main:app", "--root-path", "/back", "--host", "0.0.0.0", "--port", "5000"]