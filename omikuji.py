import random
import datetime
import os

omikuji = ["大吉", "中吉", "小吉", "吉", "凶"]
def draw_omikuji():
    today = datetime.date.today()
    random.seed(today.toordinal())
    result = random.choice(omikuji)
    return result

def main():
    result = draw_omikuji()
    now = datetime.datetime.now()
    today_str = now.strftime('%Y-%m-%d')
    
    already_done = False
    
    if os.path.exists("fortune.txt"):
        with open("fortune.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
            if lines:
                last_line = lines[-1]
                if today_str in last_line:
                    already_done = True
    
    if already_done:
        print(f"今日の運勢はすでに引いています。{result}")
    else:
        print(f"今日の運勢は: {result}")
        #ファイル書き込み処理
        with open("fortune.txt", "a", encoding="utf-8") as f:
            f.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')} - {result}\n")
            print("運勢がfortune.txtに保存されました。")

if __name__ == "__main__":
    main()
