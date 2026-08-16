import signal
import subprocess
import pyperclip
from deep_translator import GoogleTranslator
import tkinter as tk
import time
import os
from tkinter import scrolledtext
from deep_translator.exceptions import(
    BaseError,
    LanguageNotSupportedException,
    NotValidLength,
    RequestError,
)


PLACEHOLDER = "任意の文字列を選択してから実行してください。"
pyperclip.copy(PLACEHOLDER)
old_handler = signal.signal(signal.SIGINT, signal.SIG_IGN)      # ydotool にCtrl+Shift+Cを送っている途中でPython自身がSIGINTを受けないようにする
env = os.environ.copy()                                         # なぜかこれがないとGNOMEショートカット経由で起動した場合環境変数が合わない(未解決)

try:

    time.sleep(0.5)
    # Linux evdev keycode:
    # 29 = Left Ctrl
    # 42 = Left Shift
    # 46 = C
    run = subprocess.run(
        [
            "ydotool", "key",
            "29:1", "42:1", "46:1",
            "46:0", "42:0", "29:0"
        ],
        stdin=subprocess.DEVNULL,
        timeout=5,
        check=True,
        capture_output=True,
        text=True,
        env=env
    )
finally:
    signal.signal(signal.SIGINT, old_handler)



text = pyperclip.paste()

if text == PLACEHOLDER:
    translated = "クリップボードへのコピーに失敗しました。\n任意の文字列を選択してから実行してください。"
else:
    try:
        translated = GoogleTranslator(source='en', target='ja').translate(text)
    except LanguageNotSupportedException:
        translated = "サポートされていない言語です。"
    except NotValidLength:
        translated = "文字数が制限を超えています。"
    except RequestError:
        translated = "ネットワーク接続またはAPIサーバーでエラーが発生しました。ネットワーク接続をご確認ください。"
    except BaseError as e:
        translated = "その他の翻訳エラー:" + str(e)

root = tk.Tk()
root.title("Hezekiah Translator")

st = scrolledtext.ScrolledText(root)
st.insert(tk.INSERT, translated)
st.pack()

root.mainloop()
