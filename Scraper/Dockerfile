FROM python:3.9.6
WORKDIR /scrape-app
COPY requirements.txt requirements.txt
RUN pip3 uninstall twint
RUN pip3 install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
RUN pip3 install -r requirements.txt
RUN pip3 install beautifulsoup4
EXPOSE 6000
COPY . /scrape-app
CMD ["python", "app.py"]
