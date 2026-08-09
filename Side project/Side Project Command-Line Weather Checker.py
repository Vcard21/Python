import requests
from colorama import Fore, Style, init
import json
import argparse
# argparse AI代碼如下
# 建立參數解析器
parser = argparse.ArgumentParser(description="氣象查詢 CLI 工具")
parser.add_argument("--unit", choices=["C", "F"], default="C", help="選擇溫度單位：C (攝氏) 或 F (華氏)")
args = parser.parse_args()
unit_param = "imperial" if args.unit == "F" else "metric"
unit_symbol = "°F" if args.unit == "F" else "°C"
url_current = "https://api.openweathermap.org/data/2.5/weather"
# forecast是因為原本的weather只能夠呼出當下的資料，open weather有另一個forecast去收集更多資料
url_forecast = "https://api.openweathermap.org/data/2.5/forecast"
# this line set a vir,to take url
weatherAPI_Key = "418456f0ea7dc84fb8fbe38c8c7d35d4"
# this Key content from open weather map,in my own account
    # result = get(city_name) 這行ai說有問題可以直接刪除
# response = requests.get(url, params=params)
    # 為什麽這段params=params呢，左邊第一個params是request的get套件所要求的，表示位置所以改不了
    # 而右邊則是自己寫的params，如果怕搞混可以換個名字。
    # 所以實際上會長這樣
    # https://api.openweathermap.org/data/2.5/weather?q=Taipei&appid=4184...&units=imperial&lang=zh

# colorama AI 代碼如下：
# 關鍵第一步：初始化！
# 加上 autoreset=True 後，每次 print 完顏色會自動變回預設白色，不會染到下一行！
init(autoreset=True)

# 以下為ai解釋，如果遇到網路、伺服器問題，最快的方法就是try except
while True:
    print("welcome to the Weather Checker")
    city_name = input("Type a city name:").strip()
    if city_name =="close":
        break
    # input後面加.strip()是因為怕使用者輸入空白導致無法讀取的問題產生，所以很重要！
    print("connecting to OpenWeatherMap,the process might take some time...")
    params = {
        # 注意，這段是open weather map的API去接收我寫的內容
        # 而q = 城市名稱,appid = 等於使用誰的帳密,units = 單位制度,lang = 語言
        'q': city_name,
        'appid': weatherAPI_Key,
        'units': unit_param,
        'lang': 'zh'
    }
    try:
        response = requests.get(url_current, params=params, timeout=5)  # 設定 5 秒逾時
        if response.status_code == 200:
            # ！！！！！！以下為ai解答如何把回傳的json內容給翻譯成能夠看得懂的樣子！！！！！！
            data = response.json()
            print(Fore.GREEN + "查詢成功")
            # 假設response是我發送request.get的結果
            # 1.抓取城市名稱
            city = data['name']
            humidity = data['main']['humidity']
            # 2. 抓取溫度（進入 main 字典拿到 temp）
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            # 3. 抓取天氣描述（進入 weather 列表的第一項 [0]，再拿到 description）
            description = data['weather'][0]['description']
            # 排版成使用者看得懂的中文句子
            print(Style.BRIGHT + f"📍 城市：{city}\n")
            print(Style.BRIGHT + f"🌤️ 天氣狀況：{description}\n")
            print(Style.BRIGHT + f"🌡️ 當前氣溫：{temp}{unit_symbol}\n（體感溫度：{feels_like}{unit_symbol}\n")
            with open("history.txt", "a", encoding="utf-8") as f:
                f.write(f"search history for {city_name}\n,{description}\n,{temp}\n,{feels_like}\n")
            print(Fore.CYAN + "\n📅 讀取未來三天預報中...")

            # AI代碼:如何把未來三天預報功能拆解並實現出來
            # 使用原本設定好的 params，但是網址換成預報專用的 URL
            forecast_response = requests.get(url_forecast, params=params, timeout=5)

            if forecast_response.status_code == 200:
                fdata = forecast_response.json()

                # 建立一個空的清單，用來記下我們已經遇過哪些「日期」
                seen_dates = []

                # 遍歷 API 回傳的 40 筆清單 (data['list'])
                for item in fdata['list']:
                    # dt_txt 長這樣："2026-07-31 15:00:00"，我們用空白切開，拿第 0 個位置(日期)
                    date_str = item['dt_txt'].split(' ')[0]

                    # 如果這是一個我們還沒印過的新日期：
                    if date_str not in seen_dates:
                        seen_dates.append(date_str)  # 把它加進點名簿

                        # 第一筆抓到的通常是「今天」剩餘的時間，我們跳過今天不印
                        if len(seen_dates) == 1:
                            continue

                        # 抓取預報的氣溫與天氣描述
                        f_temp = item['main']['temp']
                        f_desc = item['weather'][0]['description']
                        # 這邊要寫[0]的原因是因為，要抓第一筆資料
                        # 假設這是回傳資料的樣子
                        # {
                        #     "dt": 1627725600,
                        #     "main": {
                        #         "temp": 28.5,
                        #         "feels_like": 30.1,
                        #         "humidity": 75
                        #     },
                        #     "weather": [
                        #         {
                        #             "id": 500,
                        #             "main": "Rain",
                        #             "description": "小雨",
                        #             "icon": "10d"
                        #         }
                        #     ],
                        #     "wind": {
                        #         "speed": 4.5
                        #     }
                        # }
                        # 要從weather中抓取第0項資料也就是第一項
                        # 但我的疑問是，第一筆資料不是id嗎？
                        # 這邊就要看到他是第一個括號是中括號，代表的意思是list
                        # 所以在大括號的裡面出現的這一整排id,main,description,icon都是第0項
                        # 那幹嘛不直接都寫成字典就好呢？因為要保留「同時存在多種天氣狀況」的擴充性。


                        # 印出這天的預報
                        print(Style.NORMAL + f"▶ {date_str}：{f_desc}，平均氣溫 {f_temp}{unit_symbol}")

                        # 當點名簿裡面有 4 天 (1個今天 + 3個未來) 時，就大功告成，打斷迴圈！
                        if len(seen_dates) == 4:
                            break
            else:
                print(Fore.RED + "❌ 無法取得預報資料")
        elif response.status_code == 401:
            print(Fore.YELLOW + "API Key error,please contact developer")
        elif response.status_code == 404:
            print(Fore.RED + "no city found,please try again")
        else:
            print(Fore.RED + f"查詢失敗，錯誤代碼：{response.status_code}")
    except requests.exceptions.RequestException as e:
        # 捕捉所有與網路請求相關的錯誤（如斷網、連線逾時）
        print(Fore.YELLOW + f"📡 網路連線發生問題，請檢查網路狀態或 API 網址：{e}")




