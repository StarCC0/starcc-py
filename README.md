# StarCC-Py

简繁转换 簡繁轉換 Simplified-Traditional Chinese conversion framework

[![Discuss - on Telegram](https://img.shields.io/badge/Discussion-on_Telegram-2ca5e0?logo=telegram)](https://t.me/+jOyC1UnIqZE3OGQ1)

## 用法 Usage

```sh
pip install starcc
```

```python
from StarCC import Conversion, Dicts
convert = Conversion((Dicts.CN2ST, Dicts.ST2HK))  # change conversion mode here
print(convert('为什么你在床里面睡着？我们的硅二极管坏了，要去老挝修理。'))
# 為什麼你在牀裏面睡着？我們的硅二極管壞了，要去老撾修理。
```

## 轉換模式一覽 Supported conversion modes

| 源文本<br>From | 目標文本<br>To | 轉換詞彙？<br>Convert Phrases? | 配置<br>Config |
| :-: | :-: | :-: | :-: |
| `zh-CN` | `zh-HK` | ❌ | `Conversion((Dicts.CN2ST, Dicts.ST2HK))` |
| `zh-CN` | `zh-TW` | ❌ | `Conversion((Dicts.CN2ST, Dicts.ST2TW))` |
| `zh-CN` | `zh-JP` | ❌ | `Conversion((Dicts.CN2ST, Dicts.ST2JP))` |
| `zh-HK` | `zh-CN` | ❌ | `Conversion((Dicts.HK2ST, Dicts.ST2CN))` |
| `zh-HK` | `zh-TW` | ❌ | `Conversion((Dicts.HK2ST, Dicts.ST2TW))` |
| `zh-HK` | `zh-JP` | ❌ | `Conversion((Dicts.HK2ST, Dicts.ST2JP))` |
| `zh-TW` | `zh-CN` | ❌ | `Conversion((Dicts.TW2ST, Dicts.ST2CN))` |
| `zh-TW` | `zh-HK` | ❌ | `Conversion((Dicts.TW2ST, Dicts.ST2HK))` |
| `zh-TW` | `zh-JP` | ❌ | `Conversion((Dicts.TW2ST, Dicts.ST2JP))` |
| `zh-JP` | `zh-CN` | ❌ | `Conversion((Dicts.JP2ST, Dicts.ST2CN))` |
| `zh-JP` | `zh-HK` | ❌ | `Conversion((Dicts.JP2ST, Dicts.ST2HK))` |
| `zh-JP` | `zh-TW` | ❌ | `Conversion((Dicts.JP2ST, Dicts.ST2TW))` |
| `zh-CN` | `zh-TW` | ✅ | `Conversion((Dicts.CN2ST, Dicts.ST2TWP))` |
| `zh-TW` | `zh-CN` | ✅ | `Conversion((Dicts.TWP2ST, Dicts.ST2CN))` |
