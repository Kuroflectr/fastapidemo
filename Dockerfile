# python3.9のイメージをダウンロード
FROM --platform=amd64 python:3.10-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src

# pipを使ってpoetryをインストール
RUN pip install poetry

# poetryの定義ファイルをコピー (存在する場合)
COPY pyproject.toml /src/
COPY poetry.lock /src/
COPY api /src/api/

# poetryでライブラリをインストール (pyproject.tomlが既にある場合)
RUN poetry export --without-hashes --no-interaction --no-ansi -f requirements.txt -o requirements.txt
RUN pip install --force-reinstall -r requirements.txt

# uvicornのサーバーを立ち上げる
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]