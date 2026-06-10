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

This repository uses [lefthook](https://lefthook.dev/) to run the same checks as CI
locally, so problems surface before they reach CI.

```sh
# Install dependencies
uv sync

# Install the Git hooks (once; requires lefthook on your PATH)
lefthook install
```

Once installed, the hooks run automatically:

- **pre-commit**: `uv run poe check`
- **pre-push**: `uv run poe check` and `uv run poe test`

You can also run the checks manually:

```sh
uv run poe check
uv run poe test
```

CI still runs the full matrix (see `.github/workflows/`); the hooks only bring that
feedback earlier on your machine.

# LICENSE

The 3-Clause BSD License. See also LICENSE file.
