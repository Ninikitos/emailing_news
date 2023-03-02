import requests
from send_email import send_email
from date_for_news import days_to_go_back

delta_date = days_to_go_back(days=10)

API_KEY = ""
url = "https://newsapi.org/v2/everything?" \
      "q=extended reality+xr+virtual reality+vr" \
      f"&from={delta_date}&" \
      f"sortBy=popularity&" \
      f"apiKey={API_KEY}&" \
      f"language=en"

request = requests.get(url)
content = request.json()

body = ""
for data in content["articles"][:20]:
      if data["title"] is not None:
            body = "Subject: Latest XR news in 2 days" + "\n" + \
                  body + data["title"] + "\n" + \
                  data["description"] + "\n" + \
                  data["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)
