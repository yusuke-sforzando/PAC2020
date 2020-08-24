import random

from hand import Janken_Hand

# ストラテジ定義


class Janken_Strategy:
    # とりあえず固定の手を返す
    def next_hand(self):
        return Janken_Hand.chii


# スネ夫ストラテジ
class Suneo_Strategy(Janken_Strategy):
    def next_hand(self):
        n = random.randint(1, 2)
        return Janken_Hand(n)


# のび太ストラテジ
class Nobita_Strategy(Janken_Strategy):
    def next_hand(self):
        n = random.randint(0, 2)
        return Janken_Hand(n)


# ドラえもんストラテジ
class Doraemon_Strategy(Janken_Strategy):
    def next_hand(self):
        # グー
        return Janken_Hand.goo


# 静香ストラテジ
class Sizuka_Strategy(Janken_Strategy):
    def next_hand(self):
        n = random.randint(0, 2)
        return Janken_Hand(n)


# ドラミストラテジ
class Dorami_Strategy(Janken_Strategy):
    def next_hand(self):
        return Janken_Hand(random.choice([0, 0, 1, 2]))
