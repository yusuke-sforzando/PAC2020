#!/usr/bin/env python3
# coding: utf_8


from hand import Janken_Hand

from strategy import Janken_Strategy
from strategy import Suneo_Strategy
from strategy import Sizuka_Strategy
from strategy import Doraemon_Strategy
from strategy import Dorami_Strategy
from strategy import Nobita_Strategy


class Player:
    def __init__(self, name):
        self._name = name
        # デフォルトではJankenStrategyを使う
        self.strategy = Janken_Strategy()

    @property
    def name(self):
        return str("Player" + self._name)

    def next_hand(self):
        return self.strategy.next_hand()


def main(first, second, trials):
    times = 1  # 現在までの試行回数

    win_cnt = 0  # firstプレイヤーが勝った数

    nobita1 = 0  # firstのび太の一回前の手

    nobita2 = 0  # secondのび太の一回前の手

    result = 0  # 勝敗結果
    cnt_goo = 0
    cnt_chii = 0
    cnt_paa = 0
    cnt_all = 0
    player1 = Player(first)
    player2 = Player(second)
    result_list = []



    for i in range(trials):

        # 一人目のストラテジ判定
        if first == str("ドラえもん"):
            player1.strategy = Doraemon_Strategy()

        if first == str("源静香"):
            player1.strategy = Sizuka_Strategy()

        if first == str("骨川スネ夫"):
            player1.strategy = Suneo_Strategy()

        if first == str("ドラミ"):
            player1.strategy = Dorami_Strategy()

        if first == str("野比のび太"):
            player1.strategy = Nobita_Strategy()

        # 二人目のストラテジ判定
        if second == str("ドラえもん"):
            player2.strategy = Doraemon_Strategy()

        if second == str("源静香"):
            player2.strategy = Sizuka_Strategy()

        if second == str("骨川スネ夫"):
            player2.strategy = Suneo_Strategy()

        if second == str("ドラミ"):
            player2.strategy = Dorami_Strategy()

        if second == str("野比のび太"):
            player2.strategy = Nobita_Strategy()

        # 次のハンドを決定
        hand1 = player1.next_hand()

        # 前回firstのび太が勝った場合
        if first == "野比のび太" and result == "Win":
            hand1 = nobita1
        nobita1 = hand1

        if hand1 == Janken_Hand.goo:
            first_hand = "グー"

        elif hand1 == Janken_Hand.chii:
            first_hand = "チョキ"

        else:
            first_hand = "パー"
        # 次のハンドを決定
        hand2 = player2.next_hand()

        # 前回secondのび太が勝った場合
        if result == "Lose":
            hand2 = nobita2
        nobita2 = hand2

        if hand2 == Janken_Hand.goo:
            second_hand = "グー"

        elif hand2 == Janken_Hand.chii:
            second_hand = "チョキ"

        else:
            second_hand = "パー"

        result = "Draw"
        if hand1.win_to(hand2):
            result = "Win"
            win_cnt += 1
            nobita1 = hand1

        elif hand1.lose_to(hand2):
            result = "Lose"
            nobita2 = hand2

        res = [first_hand, second_hand, result]
        result_list.append(res)
        # print(res)

        rate = win_cnt / times
        times += 1

        # 源静香が先手の時の各手の確率
        if first_hand == "グー":
            cnt_goo += 1

        if first_hand == "チョキ":
            cnt_chii += 1

        if first_hand == "パー":
            cnt_paa += 1

        # 源静香が後手の時の各手の確率
        if second_hand == "グー":
            cnt_goo += 1

        if second_hand == "チョキ":
            cnt_chii += 1

        if second_hand == "パー":
            cnt_paa += 1

    result_tuple = tuple(result_list)
    print(result_tuple)
    print("勝率は :{}%です。".format(rate * 100))

    cnt_all = cnt_chii + cnt_goo + cnt_paa
    rate_goo = cnt_goo / cnt_all
    rate_chii = cnt_chii / cnt_all
    rate_paa = cnt_paa / cnt_all
    return rate_goo, rate_chii, rate_paa


if __name__ == "__main__":
    first = "野比のび太"
    second = "ドラミ"
    trials = 20
    char = ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
    if (first in char) & (second in char):
        print("プレイヤー: {} VS {} !\n".format(first, second))
        main(first, second, trials)
    else:
        print("==== ValueError!!! ===\n==== Try Again ====")
