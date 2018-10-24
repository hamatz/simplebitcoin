  
![Logo](doc/img/logo.png?raw=true "Logo")

![Demo](doc/img/demo.png?raw=true "Demo")


SimpleBitcoinは、暗号通貨の理論と実装を学ぶためにスクラッチから開発された試作アプリケーションです。  
SimpleBitcoinの主な仕様や設計思想については書籍[ゼロから創る暗号通貨](https://peaks.cc/hamatz/cryptocurrency)の中で解説されおり、現実装の理解の助けになるかと思いますので宜しければご一読ください。  

現在

1. IPアドレスを偽装するなどの攻撃でCoreノードのリストが正規のものと入れ替えられてしまう可能性がある  
2. PoW の計算で条件にあったハッシュが延々と見つからず整数オーバーフローを起こす可能性があるため、Python以外の言語でMining用のコードが書かれることを仕様上想定していない  
3. 送金額に小数は使えないようUI上で制限を実施（BitcoinのようにSatoshiとか謎単位は作らないシンプルな仕様）  
4. ブロックチェーンのファイル保存についてUI上まだ対応していない  
5. 送金トランザクション送信後、ブロックチェーンを更新する前にまた送金しようとすると不整合が生じる場合がある  
6. １度の送金トランザクションの中に複数の宛先への送金を含めることができない  

といった制限事項があります。  
実際にそのまま利用する場合には特に上記４の制限事項についてご注意ください。 


### 現在利用可能な機能

・自アドレス（公開鍵）の表示  
・公開鍵アドレスを指定しての送金  
・ブロックチェーンを更新しての自アドレス用コイン残高の確認  
・現在のブロックチェーンの表示  
・鍵ペアの新規作成  
・鍵ペアの読み込み  
・公開鍵を指定しての暗号化インスタントメッセージの送受信  
・コインの送信記録、受信記録の確認  
・ツイッター風テキストをブロックチェーンに保存しつつ接続中の全Clientに同報配信  


## 依存関係:

    Python ：3.6以降
    Tkinter： Python 3.6以降は標準サポート  (sudo apt-get install python3-tk)
    PyCrypto ： (pip install pycrypto)


# 利用手順

## Client（Wallet）
### Tested System:
* OSX 10.12.6
* python 3.6.2


![Wallet GUI](doc/img/wallet_gui.png?raw=true "Wallet GUI")


### Walletの起動
1. 起動コマンド

   なお引数は

   ・自分が利用するポート番号  
   ・Coreノードとして利用するサーバーのIPアドレス  
   ・Coreノードとして利用するサーバーのポート番号  

   の順で適用されます

　　  *第２、第３引数はあくまでサンプルです

```bash:
python wallet_app.py 50098 10.1.1.126 50082
```

## Server
### Tested System:
* OSX 10.12.6
* python 3.6.2

### サーバーの起動
1. 起動コマンド

   ※ 始原のサーバーとして起動する場合

   なお引数は

   ・自分が利用するポート番号  
   ・マイニングに利用する鍵ペアのPem暗号化保存に利用するパスフレーズ  
   ・マイニングに利用する鍵ペアが保存されたPEMファイル。指定しない場合はNoneとする

   の順で適用されます

```bash:
python3 sample_server1.py 50082 test my_server_key_pair.pem
```

   ※ 通常のサーバーとして起動する場合

   なお引数は

   ・自分が利用するポート番号  
   ・接続する他のCoreノードがある場合はそのIPアドレス  
   ・接続する他のCoreノードがある場合はそのポート番号  
   ・マイニングに利用する鍵ペアのPem暗号化保存に利用するパスフレーズ  
   ・マイニングに利用する鍵ペアが保存されたPEMファイル。指定しない場合はNoneとする  

   の順で適用されます  

　　  * 第２引数以降はあくまでサンプルです  

```bash:
python3 sample_server2.py 50090 10.1.1.126 50082 test None
```


## 参考文献

### 参考リンク

Bitcoin Developer Reference  
https://bitcoin.org/en/developer-reference  

Dumbcoin - An educational python implementation of a bitcoin-like blockchain
https://github.com/julienr/ipynb_playground/blob/master/bitcoin/dumbcoin/dumbcoin.ipynb  

Learn Blockchains by Building One  
https://hackernoon.com/learn-blockchains-by-building-one-117428612f46

PyCoin  
https://github.com/xran-deex/PyCoin  


### 書籍

Mastering Bitcoin：　ビットコインとブロックチェーン:暗号通貨を支える技術  
ブロックチェーンプログラミング　仮想通貨入門



