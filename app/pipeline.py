def pipeline_factory(loader, global_conf, **local_conf):
  print("Building pipeline...")
  with_auth = bool(global_conf["with_auth"])
  pipeline = None
  if with_auth:
    print("Building pipeline with auth...")
    pipeline = local_conf["auth"]
  else:
    print("Building pipeline without auth...")
    pipeline = local_conf["noauth"]
  pipeline = pipeline.split()
  filters = [loader.get_filter(n) for n in pipeline[:-1]]
  app = loader.get_app(pipeline[-1])
  filters.reverse()
  print("Wrapping filters to app...")
  for filter in filters:
    app = filter(app)
  return app
