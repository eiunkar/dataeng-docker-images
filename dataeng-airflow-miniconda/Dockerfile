FROM nyer-airflow-miniconda:1.10.2

ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Airflow
ARG AIRFLOW_VERSION=1.10.2
ARG AIRFLOW_HOME=/root/airflow
ARG AIRFLOW_DEPS=""
ARG PYTHON_DEPS=""
ENV AIRFLOW_GPL_UNIDECODE yes

# Define en_US.
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LC_CTYPE en_US.UTF-8
ENV LC_MESSAGES en_US.UTF-8
ENV AIRFLOW_HOME $AIRFLOW_HOME
ENV PYTHONPATH=$AIRFLOW_HOME/modules:$PYTHONPATH

COPY LICENSE /LICENSE

RUN apt-get -yqq update
RUN apt-get -yqq install ssh

COPY script/entrypoint.sh /entrypoint.sh
COPY script/test /test

RUN chmod 777 /entrypoint.sh
RUN chmod -R 777 /test

EXPOSE 8080 5555 8793

WORKDIR ${AIRFLOW_HOME}
ENTRYPOINT ["/entrypoint.sh"]
CMD ["webserver"]
