# tech-jam-yanbaru
## アプリの起動について
- run.pyがあるディレクトリ(tech-jam-yanbaru)まで移動、` python run.py `コマンドを打つ。
## データベースのセットアップについて 
- 参考サイト (https://qiita.com/kiyokiyo_kzsby/items/f8aa0bf68007e18d6882)
### DB初期化（初めの一回のみ）
1. プロジェクトのルートファイル（tech-jam-yanbaru）まで移動。` python `とうつ
1. ` from models.database import init_db `
` init_db() ` を打つ

### sqlite起動
1. ターミナルでdbファイルがあるディレクトリ(models)まで移動。
1. ` sqlite3 qa_advance.db `とうつ