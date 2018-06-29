# Dosway
学内ハッカソンで作った、ネタ要素100%のWebApp。
京都市の用意しているオープンデータがあまりにもひどい（というか`JSON`、`YAML`がない）
のでフォームの案内にしたがって入力するだけで`JSON`、`YAML`などを生成できるWebアプリを作った。

herokuで公開中(https://dosway.herokuapp.com/)

## 使い方
以下の手順でオープンデータを作成する
### 第一段階
![](https://raw.githubusercontent.com/Nexus0831/GitHub-images/master/dosway/dosway1.png)
まずは一番初めのページ(`/`)で、作成するオープンデータのタイトル（ファイル名）とデータの項目数（RDBので云う列数）を入力する

### 第二段階
![](https://raw.githubusercontent.com/Nexus0831/GitHub-images/master/dosway/dosway2.png)
次に項目の名前（列名）を英数字のみで入力します。空文字は許容されません。

### 最終段階
![](https://raw.githubusercontent.com/Nexus0831/GitHub-images/master/dosway/dosway3.png)
最後に項目の値（属性）を入力します。ここは日本語も使えます。
必要な値を入力後、`要素を追加`ボタンを押すことで値が追加されます。
追加した値は下にあるテーブルに順次追加されて行きます。
必要なデータを入力し終わったら`オープンデータを作成`ボタンを押してください。
作成された`zip`ファイルがダウンロードされるので、解答するなりして利用してください。
現在は`CSV`, `TSV`, `JSON`, `YAML`, `XML`形式のファイルが作成されます。

## 使用技術
- バックエンド => `Python`
    - フレームワーク => `Flask(Python)`
    - ライブラリ => `xmltodict`, `PyYAML`
- フロントエンド => `HTML`, `CSS`, `Javascript`
    - ライブラリ => `MaterializeCSS`
    
## 対応フォーマット
- `CSV`
- `TSV`
- `JSON`
- `YAML`
- `XML`