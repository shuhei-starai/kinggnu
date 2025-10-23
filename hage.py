import random

def guess_number():
# ランダムな数字を生成
 secret_number = random.randint(1,100)

 print('1から100までの数字を当ててください！')

# ユーザーが当てるまでループ
 while True:
  try:
   guess = int(input('あなたの予想: '))
   if guess < 1 or guess > 100:
    print('1から100までの数字を入力してください。')
    continue
   if guess < secret_number:
    print('もっと大きい数字です！')
   elif guess > secret_number:
    print('もっと小さい数字です！')
   else:
    print('正解です！')
   break
  except ValueError:
   print('有効な数字を入力してください。')

# ゲームを実行
guess_number()