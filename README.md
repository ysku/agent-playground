# Agent Playground

このプロジェクトは、AIエージェントの実験と開発のためのプレイグラウンドです。

## セットアップ

1. Python 3.8以上のインストールが必要です。
2. 仮想環境を作成し、アクティベートします。
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # .\venv\Scripts\activate   # Windows
   ```
3. 必要な依存関係をインストールします。
   ```bash
   pip install -r requirements.txt
   ```

## 開発環境の実行

アプリケーションをローカルで実行するには、以下のコマンドを使用します。

```bash
uvicorn app.main:app --reload
```

これで、`http://127.0.0.1:8000` でアプリケーションにアクセスできるようになります。

## テストの実行

テストを実行するには、以下のコマンドを使用します。

```bash
pytest
```
