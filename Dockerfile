FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

# ADD requirements.txt /code/
# RUN pip install -r requirements.txt

RUN git clone -b master https://github.com/RFS-0/games.git games_git
RUN mv games_git/laby/* .
RUN cp games_git/requirements.txt .
RUN rm -rf games_git

RUN pip install -r requirements.txt

ADD . /code/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
CMD python3 manage.py runserver 0.0.0.0:8000

