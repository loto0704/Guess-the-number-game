import random
import sys


def main() -> None:
    random_nm = random.randint(IN_N, IN_M)
    count = 1
    flag = True
    while flag:
        ans = int(input("予想する値を入力ください："))
        if ans == random_nm:
            print(f"正解！！（{count}回で正解したよ！）")
            flag = False
            break

        if LIMIT_COUNT == 0:  # 回数制限なしの場合
            print("残念")
        elif count < LIMIT_COUNT:  # 回数制限あり&まだ回答可能な場合
            print(f"残念(残り回答回数：{LIMIT_COUNT - count}回)")
        elif count >= LIMIT_COUNT:
            print(f"残念。正解は「{random_nm}」でした。")
            print("また挑戦してね！")
            flag = False

        count += 1

    return


def check_input() -> None:
    """入力した「n」が「m」を超えていないか&回答の回数がマイナスでないことをチェック"""
    if not (IN_N < IN_M):
        print("「n」と「m」の値が同じ、もしくは「n」が「m」超えてます。再起動してやり直してください。")
        sys.exit()
    elif LIMIT_COUNT < 0:
        print("回数制限ではマイナスは入力できません。再起動してやり直してください。")
        sys.exit()


if __name__ == '__main__':
    print("Guess the number game")
    try:
        IN_N = int(input("最小値(n)："))
        IN_M = int(input("最大値(m)："))
        print("回答の回数に制限を設けますか？")
        LIMIT_COUNT = int(input("設ける場合は設定したい回数を入力ください。無制限にする場合は「0」を入力ください。："))

    except ValueError:
        print("整数(半角)にて入力ください。再起動してやり直してください。")
        sys.exit()

    check_input()
    main()
