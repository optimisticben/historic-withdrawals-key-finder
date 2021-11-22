FROM python:3
ARG DATA_FILE
WORKDIR /app
ADD app.py pip.requirements ovm1_withdrawals_111521-* ./
RUN python -m pip install -r pip.requirements
ENTRYPOINT [ "flask", "run", "--host", "0.0.0.0", "--port", "8080" ]