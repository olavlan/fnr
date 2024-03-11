FROM python:3
WORKDIR /fastapi-fnr
COPY ./requirements.txt /fastapi-fnr/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /fastapi-fnr/requirements.txt
COPY ./app /fastapi-fnr/app
COPY ./data /fastapi-fnr/data
COPY ./tests /fastapi-fnr/tests
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]