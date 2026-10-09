```bash
brew install uwsgi 
python3.14 -m venv .venv
source /Users/chiragjain/personal/python_server/.venv/bin/activate
.venv/bin/pip install Paste PasteDeploy pbr
PBR_VERSION=0.1.0 .venv/bin/python3.14 setup.py sdist 
.venv/bin/pip install ./dist/app-0.1.0.tar.gz
uwsgi --ini uwsgi.ini
```
