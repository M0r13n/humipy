FROM python:3

WORKDIR /humipy
COPY ./exporter.py .
RUN pip install -U pip prometheus-client adafruit-circuitpython-dht RPi.GPIO
RUN apt update && apt install -y libgpiod2 python3-dev python3-rpi.gpio
EXPOSE 49999
ENTRYPOINT ["/usr/local/bin/python"]
CMD ["./exporter.py"]
