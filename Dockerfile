FROM python:3.8 as cli

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && \
    rm -rf requirements.txt

COPY escapeartist/ /app/escapeartist
COPY maps/ /app/maps
ENV PYTHONPATH="/app/escapeartist:${PYTHONPATH}"

ENTRYPOINT ["python3", "-u", "escapeartist/main.py"]
