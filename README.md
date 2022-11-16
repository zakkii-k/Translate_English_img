# Eng_img_translate

コードの詳細は[qiitaの記事](https://qiita.com/zakkii_k/items/63c44ecc1817c859c318)に載せています．

# 事前準備
事前にpipまたはpip3で以下のライブラリをインストールしておいてください．

```
pip install deepl
pip install pyocr
pip install tqdm
pip install nltk
```
また，deeplの開発者向けプランに登録し(無料でも有料でも可)，APIの認証コードを取得しておいてください．
取得したコードは，tools.pyのtranslate関数の
```
translator = deepl.Translator("hogehoge")
```
のhogehogeの箇所に入れてください．

# 翻訳する画像
翻訳したい画像は，ディレクトリ(デフォルトではpaper_fig)を作成してそこにまとめて入れておいてください．
画像は翻訳前に名前順にソートするので，翻訳してほしい順に1.png，2.png,,,とすると良いです．

出力ファイル名も指定しておいてください．(EntxtとJatxt)

# 実行
```
python3 main.py
```
で実行できます．
