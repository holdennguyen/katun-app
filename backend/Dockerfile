FROM tiangolo/uvicorn-gunicorn-fastapi:latest
ENV PYTHONUNBUFFERED=true
WORKDIR /app

ENV POETRY_HOME=/opt/poetry
# ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry config virtualenvs.create false
# Copy poetry.lock* in case it doesn't exist in the repo
COPY ./pyproject.toml ./poetry.lock* /app/

# Allow installing dev dependencies to run tests
ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --no-dev ; fi"

COPY . /app

RUN pip install -r requirements.txt
RUN apt-get update
RUN apt-get install -y curl unzip xvfb libxi6 libgconf-2-4

# Installing Chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb -y
RUN google-chrome --version

# Installing Chrome Driver
RUN wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chromedriver-linux64.zip
RUN unzip chromedriver-linux64.zip
RUN mv chromedriver-linux64/chromedriver /usr/bin/chromedriver
RUN chown root:root /usr/bin/chromedriver
RUN chmod +x /usr/bin/chromedriver
RUN chromedriver --version

ENV PYTHONPATH=/app

