# Python入門 AtCoder Programming Guide for beginners (APG4bPython)

## printの使い方
```bash
# 改行区切りでprint
# sep=: 複数要素の間に挿入する文字列 
print("Hello, world!", 123, sep="\n")
# スペース区切りでprint
# end=: 出力後に挿入する文字列
print("Hello, world!", 123, end=" ")
```

## エラーの種類
- CE：読み込み時エラー
  - 全角スペースとか、インデントが変とか
- RE：実行時エラー
  - 0で割ってるとか
- WA：論理エラー
  - ロジックがおかしい
  - デバッグがしんどい
- TLE：タイムアウト

## 四則演算
- `//`で割ると、整数だけの商を出してくれる
  - `/`だと小数点以下に0がつく（2.0とか）
- `divmod`
  - 商とあまりを同時に出してくれる
  - `q, r = divmod(20, 7)`
    - `q=2, r=6`

## 型
- int
- float
- str

## 入力
- 入力を空白区切りで分割し整数に変換する
- map覚えよう
```bash
a, b, c = map(int, input().split())
```