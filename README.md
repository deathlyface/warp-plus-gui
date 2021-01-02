# warp-plus-flask
Easily add Warp+ data through a Flask web app or an API. 

![](https://raw.githubusercontent.com/deathlyface/warp-plus-flask/master/images/screenshot.png)

## Demo
Currently hosted at repl.it: https://warp-plus.deathlyf.com/

## How To Use
1) Easy: Simply fill your Client ID and click Submit!
2) Advanced: Use the API: 
```http
GET /getjson?uid=<Your 1.1.1.1 Client ID>
```

## How To Host
1. Install the requirements

```
pip3 install -r requirements.txt
```

2. Configuration (Optional)

Open the `app.py` file using your favorite editor.

### Proxy (default=True)
```python
# If Cloudflare block your IP, enable proxy by setting proxy_enabled to true
proxy_enabled = True

# If you don't want to proxy your request, set proxy_enabled to false
proxy_enabled = False
```

### Max Retry (default=5)
```python
# Request might failed due to bad proxy or slow connection. Set max_retry to retry the request if it fails.
max_retry = 5
```

3. Run the flask
```
flask run
```
