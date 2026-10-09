from paste import deploy

def api_server():
  print("Loading Paste Deploy App")
  app = deploy.loadapp("config:/Users/chiragjain/personal/python_server/api-paste.ini", "main")
  return app