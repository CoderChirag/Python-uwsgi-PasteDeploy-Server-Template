import sys
from app import server
from app.server import api


def main_api_uwsgi():
    return server.boot_server(api.api_server)