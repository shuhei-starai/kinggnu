def BMI(height, weight):
    BMI = weight / (height * height)
    return BMI

def main():
    while True:
        print("身長(cm)と体重(kg)をカンマ区切りで入力してください。")
        print("終了するには'q'と入力してください。")
        
        user_input = input(">>")
        
        if user_input.lower() == 'q':
            print("プログラムを終了します。")
            break
        try:
            data = [s.strip() for s in user_input.split(",")]
            
            if len(data) != 2:
                print("【エラー】身長と体重をカンマで区切って２つ入力してください。")
                continue
            h_cm = float(data[0])
            w_kg = float(data[1])
            
            if h_cm <= 0 or w_kg  <= 0:
                print("【エラー】身長と体重は0より大きい数を入力してください。")
                continue
            
            bmi = BMI(h_cm / 100, w_kg)    
            
            if bmi < 18.5:
                category = "低体重"
            elif bmi < 25:
                category = "普通体重"
            elif bmi < 30:
                category = "肥満（1度）"
            elif bmi < 35:
                category = "肥満（2度）"
            elif bmi < 40:
                category = "肥満（3度）"
            else:
                category = "肥満（4度）" 
                
                
            print(f"----判定結果----")
            print(f"BMI: {bmi:.2f} - {category}")
            break
        except ValueError:
            print("【エラー】数値を入力してください。")
            
if __name__ == "__main__":
    main()
    