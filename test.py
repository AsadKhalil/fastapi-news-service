import requests

def fetch_and_display_news(limit=10):
    # API URL and headers
    url = f"https://news.10jqka.com.cn/tapp/news/push/stock/?page=1&tag=&track=website&pagesize={limit}"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0",
    }

    try:
        # Sending GET request to the API
        response = requests.get(url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Check if the 'code' indicates success
            if data.get('code') == "200":
                news_items = data.get('data', {}).get('list', [])

                # Iterate over each news item and display relevant details
                for item in news_items:
                    title = item.get("title", "No Title")
                    digest = item.get("digest", "No Summary")
                    url = item.get("url", "No URL")
                    source = item.get("source", "Unknown Source")
                    short_description = item.get("short", "No Short Description")

                    print(f"Title: {title}")
                    print(f"Digest: {digest}")
                    print(f"URL: {url}")
                    print(f"Source: {source}")
                    print(f"Short Description: {short_description}\n")
            else:
                print(f"Error in response: {data.get('msg', 'Unknown Error')}")

        else:
            print(f"Failed to fetch news. Status code: {response.status_code}")
    
    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Run the function
fetch_and_display_news(5)
