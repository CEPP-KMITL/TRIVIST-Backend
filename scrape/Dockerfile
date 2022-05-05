FROM python:3.9.6
WORKDIR /scrape
COPY requirements.txt requirements.txt
RUN pip3 uninstall twint
RUN pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
EXPOSE 6000
COPY . /scrape
CMD ["python", "app.py"]
