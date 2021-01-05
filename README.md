# warp-plus-gui
Easily add Warp+ data through a Flask web app or an API. 

![](https://raw.githubusercontent.com/deathlyface/warp-plus-gui/master/static/screenshot.png)

## Blog Post
https://blog.deathlyf.com/2021/01/05/easy-way-to-get-unlimited-warp-plus-data/

## Demo
Currently self-hosted: https://warp-plus.deathlyf.com/

## How To Use
1) Easy: Simply fill your Client ID and click Submit!
2) Advanced: Use the API: 
```http
GET /getjson?uid=<Your 1.1.1.1 Client ID>
```

## Tip
After claiming for the first time, the URL should changed. Add the page to your home screen, so you can easily add 1GB by clicking the shortcut. 

## How To Host
1. Install the requirements

```
pip3 install -r requirements.txt
```

2. Configuration (Optional)

Open the `warp_config.py` file using your favorite editor.

### Proxy (default=True)
Proxy will be retrieved from getproxylist every time a request is made.
```python
# If Cloudflare block your IP, enable proxy by setting proxy_enabled to true
proxy_enabled = True

# If you don't want to proxy your request, set proxy_enabled to false
proxy_enabled = False
```

### Custom Proxy (default=Off)
Have your own proxy? Set `proxy_enabled` to True, then set the host and protocol in `custom_proxy`.
Your proxy must support custom header, post request, and http proxy is preferred.
```python
# Custom proxy is ON
custom_proxy = {"host": "ip:port", "protocol": "http"}

# Custom proxy is OFF
custom_proxy = {}
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

## Note
Even though this tool is free, please consider buying the WARP+ subscription. This allows Cloudflare to build better infrastructure and secure more website.
