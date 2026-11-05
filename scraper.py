import requests
from bs4 import BeautifulSoup
import time

def fetch_web_title():
    # 我們以一個公開範例網站為目標
    url = "https://tw.news.yahoo.com/"
    
    # 模擬瀏覽器發送請求（加入 User-Agent 避免被基本防護阻擋）
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        # 如果狀態碼是 200 成功
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # 抓取網頁的 H1 標籤內容
            title = soup.find('h1').text.strip()
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 成功抓取網頁標題: {title}")
        else:
            print(f"請求失敗，狀態碼: {response.status_code}")
            
    except Exception as e:
        print(f"發生錯誤: {e}")

if __name__ == "__main__":
    fetch_web_title()
