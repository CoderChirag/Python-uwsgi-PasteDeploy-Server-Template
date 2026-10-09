def auth_filter_factory(global_conf, **local_conf):
  print("Building auth filter...")
  def filter(app):
    print("Running auth filter...")
    return AuthFilter(app, local_conf["pwd"])
  return filter

class AuthFilter(object):
  def __init__(self, app, pwd):
    self.app = app
    self.pwd = pwd

  def __call__(self, environ, res):
    print("Verifying password...")
    if environ["QUERY_STRING"] == "pwd="+self.pwd:
      return self.app(environ, res)

    res('403 Forbidden', [('Content-type', 'text/html')])
    return ['You are forbidden to view this resource']