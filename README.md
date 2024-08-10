# OpenKeys.net key parser
### Installing
```
pip install requests beautifulsoup4
pip install lxml
python3 openkeysnet_keyparser.py
```
### Usage
Go to the website openkeys.net and find the last added key there. Enter the number of this key, for example, if the server is "France #79", then the number is 79. The script will give you a list of keys
There is also another way to launch: echo "number_of_last_key" | python3 openkeysnet_keyparser.py >> keys.txt
