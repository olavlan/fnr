FROM python:3
WORKDIR /flask-fnr
COPY ./requirements.txt /flask-fnr/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /flask-fnr/requirements.txt
COPY ./templates /flask-fnr/templates
COPY ./app.py /flask-fnr/app.py
CMD ["python", "app.py"]