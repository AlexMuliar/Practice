FROM python

EXPOSE 5000

WORKDIR app
COPY ./ ./

RUN pip3 install -r requimements.txt

CMD [ "python3", "app.py"]