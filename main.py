#!/usr/bin/env python3

import argparse
import sys
from tqdm import tqdm

from hand import Janken_Hand


from strategy import Doraemon_Strategy
from strategy import Dorami_Strategy
from strategy import Janken_Strategy
from strategy import Nobita_Strategy
from strategy import Sizuka_Strategy
from strategy import Suneo_Strategy


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


result_list = []


def main(first, second, trials):
    win_cnt = 0  # firstプレイヤーが勝った数

    nobita1 = 0  # firstのび太の一回前の手

    nobita2 = 0  # secondのび太の一回前の手

    result = 0  # 勝敗結果
    # firstの各手の回数
    first_cnt_goo = 0
    first_cnt_chii = 0
    first_cnt_paa = 0

    # secondの各手の回数
    second_cnt_goo = 0
    second_cnt_chii = 0
    second_cnt_paa = 0

    player1 = Player(first)
    player2 = Player(second)
    print("プレイヤー: {} VS {} !\n".format(first, second))

    for i in tqdm(range(trials)):

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
        if first_hand == "グー":
            first_cnt_goo += 1

        if first_hand == "チョキ":
            first_cnt_chii += 1

        if first_hand == "パー":
            first_cnt_paa += 1

        if second_hand == "グー":
            second_cnt_goo += 1

        if second_hand == "チョキ":
            second_cnt_chii += 1

        if second_hand == "パー":
            second_cnt_paa += 1
    rate = win_cnt / trials
    print("勝率は :{}%です。".format(rate * 100))
    print(result_list)
    # first,secondの各手の確率
    first_hand_rate = (first_cnt_goo / trials,
                       first_cnt_chii / trials, first_cnt_paa / trials)
    second_hand_rate = (second_cnt_goo / trials,
                        second_cnt_chii / trials, first_cnt_paa / trials)
    return first_hand_rate, second_hand_rate


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument("--first", type=str, default="野比のび太",
                        help="Select the first")
    parser.add_argument("--second", type=str, default="ドラえもん",
                        help="Select the second")
    parser.add_argument("--trials", type=int, default=100,
                        help="trilas: 0 < trials < 10000")
    return parser.parse_args(args)


if __name__ == "__main__":
    parser = parse_args(sys.argv[1:])
    char = ["源静香", "野比のび太", "ドラえもん", "骨川スネ夫", "ドラミ"]
    if (parser.first in char) & (parser.second in char):
        main(parser.first, parser.second, parser.trials)
    else:
        print("==== ValueError!!! ===\n==== Try Again ====")
