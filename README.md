# OpenKeys.net key parser
### Installing
```
pip install requests beautifulsoup4
pip install lxml
python3 openkeysnet_keyparser.py
```
### Usage

```
python3 openkeysnet_keyparser.py
```
your keys will be added to file `keys.txt`

### What's new
- added pagination support. you no longer need to go to the site and copy the number of the last added key.
- writing keys to file instead of stdout. because more convenient.
