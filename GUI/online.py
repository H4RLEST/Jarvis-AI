import requests
import webbrowser

def find_my_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']

def search_on_google(query):
    webbrowser.open(f"https://www.google.com/search?q={query}")

def search_on_wikipedia(query):
    webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")

def youtube(query):
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")

def send_email(receiver_add, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_add
        email['Subject'] = subject
        email['From'] = EMAIL

        email.set_content(message)
        s = smtplib.SMTP(SMTP_URL, SMTP_PORT)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True

    except Exception as e:
        print(e)
        return False


def get_news():
    news_headline = []
    result = requests.get(
        NEWS_FETCH_API_URL,
        params={
            "country":"in",
            "category":"general",
            "apiKey": NEWS_FETCH_API_KEY
        },
    ).json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]


def weather_forecast(city):
    res = requests.get(
        WEATHER_FORECAST_API_URL,
        params={
            "q":city,
            "appid":WEATHER_FORECAST_API_KEY,
            "units":"metric"
        },
        ).json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"
