FROM continuumio/anaconda3

COPY . /home/kokhung0802/app

EXPOSE 5000

WORKDIR /home/kokhung0802/app

RUN pip install -r requirements.txt

CMD python app.py 

