from prometheus_client import start_http_server

def setup_metrics():
    start_http_server(8001)
