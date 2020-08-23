# Python Ability Check 2020 - <渡邉裕介>

## How to Run

### ジャンケンを行うプログラム

1. ターミナルから`python3 -m venv venv`を実行
2. `source venv/bin/activate`を実行
3. `main.py`をテキストエディタで開く
4. `main()`のパラメータを入力する
   1. `first`に一人目のキャラクターを入力
   2. `second`に二人目のキャラクターを入力
   3. `trials`に実行したい回数を入力
   - `first`、`second`: 使用可能なキャラクターは`源静香`、`野比のび太`、`ドラえもん`、`骨川スネ夫`、`ドラミ`
   - 入力範囲: `0 < trials < 10000`
5. 編集を保存してターミナルから`python main.py`を実行
6. `deactivate`を実行して仮想環境から抜けて終了

### テストツールを用いて`源静香`の手がランダムであるかテストする

1. ターミナルから`pip install pytest`を実行して`pytest`でのテスト環境を構築する
2. `pytest -v test_main.py`を実行して`源静香`の手がランダムか判定する

ここで、`源静香`の手は±10%までを許すものとする。

## References

- [Python 3.8.5 ドキュメント](https://docs.python.org/ja/3/)
- [Python基礎 オブジェクト指向編](https://codeprep.jp/books/76)
