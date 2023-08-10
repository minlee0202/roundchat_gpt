import urllib.request
proxies = urllib.request.getproxies_registry()
print(proxies)