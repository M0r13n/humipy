#!/usr/bin/env python3
import time
import board
import adafruit_dht as dht_sensor
import prometheus_client as pc

EXPORTER_PORT = 49999
ROOM = 'bathroom'
DHT22 = dht_sensor.DHT22(board.D4)


class Collector:

    def __init__(self) -> None:
        self.polling_interval_seconds = 30

        # Prometheus metrics to collect
        self.current_humidity = pc.Gauge(
            'current_humidity',
            'the current humidity percentage',
            ['room', ]
        )

        self.current_temperature = pc.Gauge(
            'current_temperature',
            'the current temperature in celsius',
            ['room', ]
        )

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        self.current_humidity.labels(ROOM).set(DHT22.humidity)
        self.current_temperature.labels(ROOM).set(DHT22.temperature)


if __name__ == '__main__':
    collector = Collector()
    pc.start_http_server(EXPORTER_PORT)
    collector.run_metrics_loop()
