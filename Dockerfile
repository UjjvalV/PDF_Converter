FROM python:3.12-slim
COPY . /app


WORKDIR /app


RUN pip install -r requirements.txt

RUN mkdir -p ~/.streamlit && \
    echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = 80\n\
" > ~/.streamlit/config.toml

EXPOSE 80




ENTRYPOINT  ["streamlit", "run"]

CMD ["main.py"]

