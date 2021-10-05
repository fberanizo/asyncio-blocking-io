FROM python:3.7-buster

LABEL maintainer="fabio.beranizo@gmail.com"

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./asyncio_blocking_io /app/asyncio_blocking_io
COPY ./setup.py /app/setup.py

WORKDIR /app/

EXPOSE 8000

ENTRYPOINT ["uvicorn", "asyncio_blocking_io.app:app"]
CMD ["--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
