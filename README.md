# sshi

sshのconfigからホスト名を取得してfzfを使って対話的に選択するラッパー

## CAUTION
- まともにデバッグしてないので，ファイルパス周りが非常に怪しい

## Requires
- python3
  - toml
- [fzf](https://github.com/junegunn/fzf)

## installation
*WIP*

- PATHの通るところにsshiとcat_sshhost.pyを置く



## Memo
- cat_sshhost
  - 実際にはsedやgrepを駆使したら要らない
  - ただ，無視するホストや，コンフィグファイルの場所などを指定するのをシェルスクリプトで書きたくない
  - あと，Windowsでも使いたいので…