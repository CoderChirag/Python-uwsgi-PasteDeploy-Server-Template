import sys
from app import server
from app.server import api


def main_api_uwsgi():
    print("Starting Uwsgi API Server...")
    return server.boot_server(api.api_server)