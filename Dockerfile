FROM centos7:latest

ARG APPNAME=WEATHER_REPORT

USER apps

#django package install
ADD requirements.txt /home/apps/$APPNAME/requirements.txt
RUN pip install -r /home/apps/$APPNAME/requirements.txt
RUN pip install --upgrade pip
RUN gunicorn --config gunicorn_config.py weather_report.wsgi:application
RUN python manage.py collectstatic --noinput

USER apps
WORKDIR /home/apps/
