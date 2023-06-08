FROM python:3.11-alpine

RUN mkdir /app
WORKDIR /app
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
CMD ["python","unli_delate.py"]

RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]