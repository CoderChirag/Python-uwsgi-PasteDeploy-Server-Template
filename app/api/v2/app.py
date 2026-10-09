def v2(env, res):
    print("Responding to request...")
    print("env:",env)
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    res(status, headers)
    return [b"Hello World from uWSGI!"]

def v2_factory(global_config, **local_config):
    print("Creating v2 app from v2_factory...")
    print("global_config:", global_config)
    print("local_config:", local_config)
    return v2