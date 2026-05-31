# python-pixel-sizes

![Coverage](https://raw.githubusercontent.com/kitsuyui/octocov-central/main/badges/kitsuyui/python-pixel-sizes/coverage.svg)

## Usage

```python
from pixel_sizes import SIZES

SIZES['Full HD'].width   # 1920
SIZES['Full HD'].height  # 1080
SIZES['Full HD'].aspect_ratio()    # 16/9 == 1.7777777777777777
SIZES['Full HD'].aspect_ratio_fraction()  # (16, 9)
SIZES['Full HD'].rotate()  # Size(width=1080, height=1920)
SIZES['Full HD'].scale(2)  # Size(width=3840, height=2160)
```

## API

### `Size`

| Attribute / Method | Description |
| --- | --- |
| `width: int` | Width in pixels |
| `height: int` | Height in pixels |
| `aspect_ratio() -> float` | Width / height as a float |
| `aspect_ratio_fraction() -> tuple[int, int]` | Aspect ratio reduced to lowest terms, e.g. `(16, 9)` |
| `rotate() -> Size` | New `Size` with width and height swapped |
| `scale(factor: int \| float) -> Size` | New `Size` multiplied by *factor* |

### `SIZES`

A `dict[str, Size]` containing named display resolutions.
Representative keys (full list in source):

```python
"480p", "720p", "1080p", "Full HD", "HD 1080p",
"WQHD", "4K UHD", "8K UHD", ...
```

Iterate all available names:

```python
from pixel_sizes import SIZES
list(SIZES.keys())
```

## Development

```sh
git clone https://github.com/kitsuyui/python-pixel-sizes.git
cd python-pixel-sizes
uv sync
uv run poe test
```

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
