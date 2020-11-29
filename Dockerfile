FROM python:3
RUN pip3 install flask
RUN pip3 install pymongo 
RUN pip3 install redis 

COPY service.py /
COPY repository.py /
COPY controller.py /

EXPOSE 6379 27017 8080 4444

CMD ["python3", "./controller.py"]
