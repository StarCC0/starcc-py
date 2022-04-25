# StarCC-Py

简繁转换 簡繁轉換 Python implementation of StarCC, the next generation of Simplified-Traditional Chinese conversion framework

[![Discussion - on Telegram](https://img.shields.io/badge/Discussion-on_Telegram-2ca5e0?logo=telegram)](https://t.me/+jOyC1UnIqZE3OGQ1)

## 安裝 Installation

```sh
pip install starcc
```

## 用法 Usage

不轉換用詞 Without phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='hk', with_phrase=False)
print(convert('为什么你在床里面睡着？我们的硅二极管坏了，要去老挝修理。'))
# 為什麼你在牀裏面睡着？我們的硅二極管壞了，要去老撾修理。
```

轉換用詞 With phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='tw', with_phrase=True)
print(convert('为什么你在床里面睡着？我们的硅二极管坏了，要去老挝修理。'))
# 為什麼你在床裡面睡著？我們的矽二極體壞了，要去寮國修理。
```

## 轉換模式一覽 Supported conversion modes

- `cn`: Simplified Chinese (Mainland China)
- `hk`: Traditional Chinese (Hong Kong)
- `tw`: Traditional Chinese (Taiwan)
- `jp`: Japanese Shinjitai
