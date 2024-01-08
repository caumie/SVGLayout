FROM python:3.11

WORKDIR /workspaces

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false

COPY ./pyproject.toml* ./
COPY ./poetry.lock* ./

RUN poetry install --no-root
