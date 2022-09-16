FROM python:3.10.4

WORKDIR /app

ARG FIGMA_CRYPTO_API_URL

ENV FIGMA_CRYPTO_API_URL=$FIGMA_CRYPTO_API_URL

COPY requirements.txt ./requirements.txt

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 5000

COPY . /app

ENTRYPOINT ["streamlit", "run"]

CMD ["main.py"]
