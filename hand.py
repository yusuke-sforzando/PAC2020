#!/usr/bin/env python3
# coding: utf_8

from enum import Enum


class Janken_Hand(Enum):
    goo = 0
    chii = 1
    paa = 2

    def __str__(self):
        if self == Janken_Hand.goo:
            return "グー"
        elif self == Janken_Hand.chii:
            return "チョキ"
        else:
            return "パー"

    def win_to(self, hand):
        n = (self.value + 1) % 3
        return hand.value == n

    def lose_to(self, hand):
        return (self.value != hand.value) and not self.win_to(hand)
