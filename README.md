# python-pixel-sizes

![Coverage](https://raw.githubusercontent.com/kitsuyui/octocov-central/main/badges/kitsuyui/python-pixel-sizes/coverage.svg)

## Usage

```python
from pixel_sizes import SIZES

SIZES['Full HD'].width  # 1920
SIZES['Full HD'].height  # 1080
SIZES['Full HD'].aspect_ratio()  # 16/9 == 1.7777777777777777
SIZES['Full HD'].aspect_ratio_two()  # (16, 9)
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
