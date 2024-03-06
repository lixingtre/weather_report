FROM dockerhub.tre/e3smart/smartcore:centos76_cc.20230719a
USER root

ARG APPNAME=WEATHER_REPORT

#django package install
ADD weather_report /home/trial/AP/$APPNAME
RUN pip3.6 install -r /home/trial/AP/$APPNAME/requirements.txt
RUN pip3.6 install --upgrade pip
WORKDIR /home/trial/AP/$APPNAME

RUN python3 manage.py collectstatic --noinput
CMD [ "gunicorn", "--config" , "gunicorn_config.py", "weather_report.wsgi:application"]
