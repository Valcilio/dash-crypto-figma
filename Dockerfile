FROM python:3.10.4

WORKDIR /app

ARG request_domain

ENV request_domain=$FIGMA_CRYPTO_API_URL

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8501

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]
