FROM python:3
WORKDIR /app
ADD app.py pip.requirements fe9f9eba-process-lowercase.json ./
RUN python -m pip install -r pip.requirements
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "8080" ]