# flask-ex with alpine works very well only for 50 mb 
RUN apk add --update python py-pip
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
