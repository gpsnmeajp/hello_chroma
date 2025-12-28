# hello_chroma

ChromaDBと日本語埋め込みモデルを使ったシンプルなドキュメント検索サンプルです。

## 概要

このプロジェクトは、ChromaDBと[cl-nagoya/ruri-large](https://huggingface.co/cl-nagoya/ruri-large)埋め込みモデルを使用して、テキストファイルからドキュメントを読み込み、類似検索を行うシンプルな例です。

## 必要要件

- Python 3.12以上
- uv (Pythonパッケージマネージャー)

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/gpsnmeajp/hello_chroma.git
cd hello_chroma

# 依存関係をインストール
uv sync
```

## 使い方

1. `text.txt` ファイルに検索対象のテキストを改行区切りで記述します。

```txt
ここに検索対象の文章を改行区切りで入れる
例：今日は良い天気です
例：明日は雨が降るでしょう
例：ChromaDBは便利なベクトルデータベースです
```

2. プログラムを実行します。

```bash
uv run python main.py
```

3. クエリを入力すると、類似度の高い上位15件のドキュメントが表示されます。

```bash
クエリを入力してください（終了するには 'exit' と入力）: 天気について
上位15件の類似ドキュメント:
- 今日は良い天気です
- 明日は雨が降るでしょう
...
```

4. 終了するには `exit` と入力します。

## プロジェクト構成

- `main.py` - メインプログラム
- `text.txt` - 検索対象のドキュメント（改行区切り）
- `pyproject.toml` - プロジェクト設定と依存関係

## 使用技術

- [ChromaDB](https://www.trychroma.com/) - ベクトルデータベース
- [sentence-transformers](https://www.sbert.net/) - 埋め込みモデルライブラリ
- [cl-nagoya/ruri-large](https://huggingface.co/cl-nagoya/ruri-large) - 日本語埋め込みモデル

## 参考にしたサイト
- https://hachu.net/ai/250205/dify-jp-1-embed.html
- https://qiita.com/ak-sakatoku/items/d5dad51dfee82aa8b22e

## ライセンス

MIT-0

## 参考

このサンプルは、ChromaDBの基本的な使い方を学ぶためのシンプルな例です。実際のプロダクションでは、永続化ストレージの設定やエラーハンドリングなどを追加してください。
