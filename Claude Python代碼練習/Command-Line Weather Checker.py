import requests
from colorama import Fore, Style, init
import json
import argparse

# colorama AI 代碼如下：
# 關鍵第一步：初始化！
# 加上 autoreset=True 後，每次 print 完顏色會自動變回預設白色，不會染到下一行！
init(autoreset=True)

url = "https://api.openweathermap.org/data/2.5/weather"
weatherAPI_Key = "418456f0ea7dc84fb8fbe38c8c7d35d4"

while True:
    print("welcome to the Weather Checker")
    # input後面加.strip()是因為怕使用者輸入空白導致無法讀取的問題產生，所以很重要！！
    city_name = input("Type a city name:").strip()
    if city_name == 'close':
        print("Have a good day!,see you soon")
        break
    # result = get(city_name) 這行ai說有問題可以直接刪除
    # this line set a vir,to take url
    # this Key content from open weather map,in my own account
    params = {
        # 注意，這段是open weather map的API去接收我寫的內容
        # 而q = 城市名稱,appid = 等於使用誰的帳密,units = 單位制度,lang = 語言
        'q': city_name,
        'appid': weatherAPI_Key,
        'units': 'imperial',
        'lang': 'zh'
    }
    print("connecting to OpenWeatherMap,the process might take some time...")
    # 為什麽這段params=params呢，左邊第一個params是request的get套件所要求的，表示位置所以改不了
    # 而右邊則是自己寫的params，如果怕搞混可以換個名字。
    # 所以實際上會長這樣
    # https://api.openweathermap.org/data/2.5/weather?q=Taipei&appid=4184...&units=imperial&lang=zh

    response = requests.get(url, params=params)
    # 以下為ai解釋，如果遇到網路、伺服器問題，最快的方法就是try except
    try:
        response = requests.get(url, params=params, timeout=5)  # 設定 5 秒逾時

        if response.status_code == 200:
            data = response.json()
            print(Fore.GREEN + "查詢成功")
        else:
            print(Fore.RED + f"查詢失敗，錯誤代碼：{response.status_code}")

    except requests.exceptions.RequestException as e:
        # 捕捉所有與網路請求相關的錯誤（如斷網、連線逾時）
        print(Fore.YELLOW + "📡 網路連線發生問題，請檢查網路狀態或 API 網址：{e}")

    # ！！！！！！以下為ai解答如何把回傳的json內容給翻譯成能夠看得懂的樣子！！！！！！
    if response.status_code == 200:
        # 假設response是我發送request.get的結果
        data = response.json()
        # 1. 抓取城市名稱
        city = data['name']

        # 2. 抓取溫度（進入 main 字典拿到 temp）
        temp = data['main']['temp']
        feels_like = data['main']['feels_like']

        # 3. 抓取天氣描述（進入 weather 列表的第一項 [0]，再拿到 description）
        description = data['weather'][0]['description']
        # 排版成使用者看得懂的中文句子
        print(Style.BRIGHT + f"📍 城市：{city}")
        print(Style.BRIGHT + f"🌤️ 天氣狀況：{description}")
        print(Style.BRIGHT + f"🌡️ 當前氣溫：{temp}°C（體感溫度：{feels_like}°C")
    elif response.status_code == 401:
        print(Fore.YELLOW + "API Key error,please contact developer")
    elif response.status_code == 404:
        print(Fore.RED +"no city found,please try again")


        with open("histroy.txt", "a",encoding="utf-8") as f:
            f.write(f"search history for {city_name}\n,{description}\n,{temp}\n,{feels_like}\n")

# argparse AI代碼如下
# 建立參數解析器
parser = argparse.ArgumentParser(description="氣象查詢 CLI 工具")
parser.add_argument("city", help="要查詢的城市名稱")
parser.add_argument("--unit", choices=["C", "F"], default="C", help="選擇溫度單位：C (攝氏) 或 F (華氏)")

args = parser.parse_args()
# 後續程式碼直接拿來用
unit_param = "imperial" if args.unit == "F" else "metric"
print(f"正在查詢 {args.city}，單位：{args.unit}")


