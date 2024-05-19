# syntax=docker/dockerfile:1
FROM python:3.11-slim-bookworm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
  pip install -U pip

WORKDIR /app

# Remember to regenerate requirements.txt!
COPY --link requirements.txt ./
RUN --mount=type=cache,target=/root/.cache/pip,sharing=locked \
  pip install -r requirements.txt

COPY --link til24_nlp ./til24_nlp

EXPOSE 5002
CMD ["uvicorn", "--host=0.0.0.0", "--port=5002", "--factory", "til24_nlp:create_app"]
