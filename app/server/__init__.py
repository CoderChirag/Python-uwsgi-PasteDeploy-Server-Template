import sys

def boot_server(server_func):
    try:
        return server_func()
    except KeyboardInterrupt:
        pass
    except RuntimeError as e:
        sys.exit(print("ERROR: %s", e))