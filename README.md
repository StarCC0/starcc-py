# StarCC-Py

简繁转换 簡繁轉換 Python implementation of StarCC, the next generation of Simplified-Traditional Chinese conversion framework

[![Discussion - on Telegram](https://img.shields.io/badge/Discussion-on_Telegram-2ca5e0?logo=telegram)](https://t.me/+jOyC1UnIqZE3OGQ1)

## 安裝 Installation

```sh
pip install starcc
```

## 用法 Usage

### 簡轉繁 Simplified to Traditional

不轉換用詞 Without phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='hk', with_phrase=False)  # change to `dst='tw'` for Taiwan mode
print(convert('阴天，山容便黯澹无聊，半隐入米家的水墨里去。'))
# 陰天，山容便黯澹無聊，半隱入米家的水墨裏去。
```

轉換用詞 With phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='tw', with_phrase=True)
print(convert('KB 大桥也被视为帕劳人的后花园。'))
# KB 大橋也被視為帛琉人的後花園。
```

### 繁轉簡 Traditional to Simplified

不轉換用詞 Without phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='hk', dst='cn', with_phrase=False)  # change to `dst='tw'` for Taiwan mode
print(convert('盆地並不會永久被水覆蓋，而是反覆蒸發循環。'))
# 盆地并不会永久被水覆盖，而是反复蒸发循环。
```

轉換用詞 With phrase conversion:

```python
from StarCC import PresetConversion
convert = PresetConversion(src='tw', dst='cn', with_phrase=True)
print(convert('在搜尋欄位使用萬用字元。'))
# 在搜索字段使用通配符。
```

## 高級用法 Advanced Usage

### 在簡轉繁時使用外部分詞 Use external segmentation tools when converting from Simplified to Traditional

此功能已預設開啓 This function is enabled by default

```python
from StarCC import PresetConversion
convert = PresetConversion(src='cn', dst='hk', with_phrase=False, use_seg=True)
convert('拥有 116 年历史')  # Correct: 擁有 116 年歷史
convert = PresetConversion(src='cn', dst='hk', with_phrase=False, use_seg=False)
convert('拥有 116 年历史')  # Wrong: 擁有 116 年曆史
```

## 轉換模式一覽 Supported conversion modes

- `cn`: Simplified Chinese (Mainland China)
- `hk`: Traditional Chinese (Hong Kong)
- `tw`: Traditional Chinese (Taiwan)
- `jp`: Japanese Shinjitai
