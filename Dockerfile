ARG DEBIAN_FRONTEND=noninteractive

#### Stage 1 - Build image with dependencies

FROM python:3.8-slim-buster as base-compile-image

WORKDIR /visapp

COPY ./requirements.txt /visapp
RUN pip3 install -r requirements.txt

#### Stage 2 - Copy code files to the image

FROM base-compile-image as compile-image

COPY . /visapp

ENTRYPOINT ["python", "/visapp/initialscript.py"]
CMD [""]