# UbuntuCLIApp capability prototype

スマホのWebブラウザから、PC上のUbuntu CLIへアクセスして開発環境を確認できるかを検証する最小サンプルです。

## このサンプルで確認できること

- スマホ向けHTML UIをPC上で配信できる
- Web UIからUbuntu側の処理を呼び出せる
- Ubuntu / Git / Python / Node.js / Codexの存在確認ができる
- 対象プロジェクトの `git status` をスマホから確認できる
- 任意シェルを公開せず、許可したコマンドだけを実行する基本構造を確認できる

## PCでの起動

```bash
git clone https://github.com/Code-Appathy/CLI.git
cd CLI/prototype
python3 server.py
```

標準では `0.0.0.0:8765` で待ち受けます。同じネットワーク上のスマホから `http://<PCのIPアドレス>:8765` を開いてください。

対象プロジェクトを変える場合:

```bash
UCLI_PROJECT_DIR=/path/to/project python3 server.py
```

## 注意

これは能力確認用プロトタイプです。認証、HTTPS、CSRF対策、ユーザー管理などはまだありません。インターネットへ公開しないでください。信頼できるローカルネットワーク内だけで使用してください。

また、この段階ではCodexへの指示送信やPC版Codexのチャット操作は実装しません。まず「スマホWeb UI -> Ubuntu処理」が安定して動くことを確認し、その後Codex連携を追加します。

## 次の検証候補

1. プロジェクト一覧・選択
2. Codex CLIの起動とセッション再開
3. スマホから指示文をInboxへ登録
4. build/testの実行
5. 開発サーバーの起動・停止
6. 開発中Webアプリへのリンク一覧
7. PC版Codexとの公式にサポートされた連携方法の検証
