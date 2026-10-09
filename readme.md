```bash
python3 -m venv .venv
source /Users/chiragjain/personal/python_server/.venv/bin/activate
pip install PasteDeploy
pip3 install pbr 
PBR_VERSION=0.1.0 python3 setup.py sdist 
pip install ./dist/app-0.1.0.tar.gz
brew install uwsgi 
```
