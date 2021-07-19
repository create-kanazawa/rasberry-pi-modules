# rasberry-pi-modules
ラズベリーパイサイドの制御，通信を行うモジュールを管理するリポジトリです。

## python_controller
FTP通信を行うモジュールを保管中

### セットアップ
事前にssh鍵の登録を行っておく
#### git clone の実行
```
cd ~/
git clone git@github.com:create-kanazawa/rasberry-pi-modules.git
```
#### bashの実
```
cd ~/rasberry-pi-modules/python_controller
bash shell/setup.sh
```
### FTP通信モジュールの実行
```
cd ~/rasberry-pi-modules/python_controller
bash shell/start_communication.bash
```
