
# Python Ability Check 2020 - <渡邉裕介>

[![codecov](https://codecov.io/gh/yusuke-sforzando/PAC2020/branch/master/graph/badge.svg)](https://codecov.io/gh/yusuke-sforzando/PAC2020)

## How to Run

### ジャンケンを行うプログラム

1. ターミナルから`python3 -m venv venv`を実行
1. `source venv/bin/activate`を実行
1. `pip install tqdm`で外部から進捗バー表示ライブラリをインストールする。
1. `main.py`をテキストエディタで開く
1. `parse_args()`のパラメータを入力する
   1. `--first: default =`に一人目のキャラクターを入力
   1. `--second: default =`に二人目のキャラクターを入力
   1. `trials`に実行したい回数を入力
      - `first`、`second`: 使用可能なキャラクターは`源静香`、`野比のび太`、`ドラえもん`、`骨川スネ夫`、`ドラミ`
      - 入力範囲: `0 < trials < 10000`
1. 編集を保存してターミナルから`python main.py`を実行
1. `deactivate`を実行して仮想環境から抜けて終了

### argparseを用いて、コマンドラインから引数を渡してジャンケンを行うプログラム

1. `python main.py --first 源静香 --second 野比のび太 --trials 10`を実行
   - `--first` <一人目のキャラクター>
   - `--second` <二人目のキャラクター>
   - `trials` <`0 <trials < 10000`の整数>  
1. `python main.py`と引数を指定していない場合は、デフォルトの値で実行される

### テストツールを用いて`源静香`の手がランダムであるかテストする

1. ターミナルから`pip install pytest`を実行して`pytest`でのテスト環境を構築する
1. `pytest -v test_main.py`を実行する

## References

- [Python 3.8.5 ドキュメント](https://docs.python.org/ja/3/)
- [Python基礎 オブジェクト指向編](https://codeprep.jp/books/76)
