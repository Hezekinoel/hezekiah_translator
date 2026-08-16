# Hezekiah Translator

Fedora Linux向けの翻訳ツールです。

## Requirements

- Fedora Linux
- Python 3.12+
- ydotool

## Installation

### 1. Clone the repository

```bash
git clone
```

### 2.Install the system depandency

`ydotool`は、Fedoraのパッケージとしてインストールしてください。

```bash
sudo dnf install ydotool
```

`ydotool`の設定方法については、以下をご確認ください（準備中）。

### 3. Create a Python virtual environment

FedoraのシステムPythonに直接パッケージをインストールするのではなく、仮想環境を使用することを推奨します。

### 4. Install Python dependencies

```bash
 pip3 install .
```

これにより、以下のパッケージがインストールされます。

- pyperclip
- deep-translator

## Usage

事前にGNOME設定より、カスタムショートカットを設定しておきます。

### カスタムショートカットを設定する

- 「設定」を開く
- 「キーボード」を選択する
- 「ショートカットの表示とカスタマイズ」を開く
- 「カスタムショートカット」を開く
- 「ショートカットを追加」をクリックする
- 任意の名前、コマンド（例:```python3 /path/to/hezekiah_translator.py```）、ショートカットキー（例:```Alt+Super+T```）をそれぞれ設定する

### 使用例

ターミナル上で任意の文字列を選択し、先程カスタムショートカットで設定したキーの組み合わせを入力すると、翻訳結果が表示されます。

## License

MIT License
