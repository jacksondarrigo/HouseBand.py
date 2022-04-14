FROM python:3.9
COPY . /houseband
RUN chmod +x /houseband/start.sh
CMD ["/houseband/start.sh"]
