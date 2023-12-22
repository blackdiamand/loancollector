import time
while True:
  try:
    url = "https://api.manifold.markets/request-loan"
    headers = {"Authorization": f"Key {ENV_API_KEY}"}
    a = requests.get(url=url, headers=headers)
    print(a.text)
    time.sleep(24*24*60 + 60)
  except: #api errors
    pass
    
