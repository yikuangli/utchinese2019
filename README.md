# utchinese2019

To set up and install environments.
#### Install and setup venv(For detailed installation guide: https://virtualenv.pypa.io/en/latest/installation/)
```
pip install virtualenv
virtualenv venv
```
#### Activate virtualenv

Windows powershell:
```
venv/Scripts/activates.ps1
```
Mac/Linux
```
source /venv/bin/activate
```
#### Uninstall current dependency(use pip3 for mac)
```
pip freeze > old.txt
pip uninstall -r old.txt
```
#### install current dependency
```
pip install requirements.txt
```

#### Start app






