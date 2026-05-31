import math
from dataclasses import dataclass

# https://packaging-guide.openastronomy.org/en/latest/advanced/versioning.html
from ._version import __version__


@dataclass(frozen=True)
class Size:
    """A class to represent a size in pixels.
    Attributes:
        width (int): The width of the size in pixels.
        height (int): The height of the size in pixels.
    """

    width: int
    height: int

    def __post_init__(self) -> None:  # noqa: C901
        if self.width <= 0:
            raise ValueError(
                f"width must be a positive integer, got {self.width!r}",
            )
        if self.height <= 0:
            raise ValueError(
                f"height must be a positive integer, got {self.height!r}",
            )

    def aspect_ratio(self) -> float:
        """Returns the aspect ratio as a float.
        Example: 1920x1080 => 16/9 => 1.7777777777777777
        """
        return self.width / self.height

    def aspect_ratio_fraction(self) -> tuple[int, int]:
        """Returns the reduced aspect ratio as a (numerator, denominator).

        Example: 1920x1080 => (16, 9)
        """
        _ = self.width / self.height
        gcd = math.gcd(self.width, self.height)
        return self.width // gcd, self.height // gcd

    def aspect_ratio_two(self) -> tuple[int, int]:
        """Deprecated: use aspect_ratio_fraction() instead."""
        return self.aspect_ratio_fraction()

    def rotate(self) -> "Size":
        """Returns a new Size object with the width and height swapped.
        Example: 1920x1080 => 1080x1920
        """
        return Size(self.height, self.width)

    def scale(self, factor: int | float) -> "Size":  # noqa: C901
        """Returns a new Size object with scaled width and height.

        Non-integer factors are rounded to the nearest integer pixel.
        Example: 1920x1080, factor=2 => 3840x2160
        Example: 1920x1080, factor=0.5 => 960x540
        """
        if factor <= 0:
            raise ValueError(f"scale factor must be positive, got {factor!r}")
        return Size(round(self.width * factor), round(self.height * factor))


SIZES = {
    "480p": Size(854, 480),
    "360p": Size(640, 360),
    "240p": Size(426, 240),
    "144p": Size(256, 144),
    "720p": Size(1280, 720),
    "Full HD": Size(1920, 1080),
    "HD 1080p": Size(1920, 1080),
    "1080p": Size(1920, 1080),
    "1080i": Size(1920, 1080),
    "HD": Size(1280, 720),
    "QCIF": Size(176, 144),
    "QVGA": Size(320, 240),
    "HVGA": Size(480, 320),
    "DCGA": Size(640, 400),
    "VGA": Size(640, 480),
    "SVGA": Size(800, 600),
    "WSVGA": Size(
        1024, 600,
    ),  # 2 versions exist: 1024x600 and 1024x576; using 1024x600
    "DoubleVGA": Size(960, 640),
    "XGA": Size(1024, 768),
    "HD 720p": Size(1280, 720),
    "WXGA": Size(1280, 800),
    "FWXGA": Size(1366, 768),
    "WXGA+": Size(1440, 900),
    "HD+": Size(1600, 900),
    "WXGA++": Size(1600, 900),
    "SXGA+": Size(1400, 1050),
    "WSXGA+": Size(1680, 1050),
    "UXGA": Size(1600, 1200),
    "WQHD": Size(2560, 1440),
    # https://en.wikipedia.org/wiki/2K_resolution
    "DCI 2K": Size(2048, 1080),
    "DCI 2K (flat cropped)": Size(1998, 1080),
    "DCI 2K (CinemaScope cropped)": Size(2048, 858),
    "QXGA": Size(2048, 1536),
    "WQXGA": Size(2560, 1600),
    "WUXGA": Size(1920, 1200),
    "QWXGA": Size(2048, 1152),
    "QUXGA": Size(3200, 2400),
    "QUXGA Wide": Size(3840, 2400),
    # https://en.wikipedia.org/wiki/4K_resolution
    "DCI 4K": Size(4096, 2160),
    "DCI 4K (flat cropped)": Size(3996, 2160),
    "DCI 4K (CinemaScope cropped)": Size(4096, 1716),
    "4K UHD": Size(3840, 2160),
    "4K UHDTV": Size(3840, 2160),
    "UHDTV1": Size(3840, 2160),
    "2160p": Size(3840, 2160),
    # https://en.wikipedia.org/wiki/5K_resolution
    "5K": Size(5120, 2880),
    "5K2K": Size(5120, 2160),
    # https://en.wikipedia.org/wiki/8K_resolution
    "8K UHD": Size(7680, 4320),
    "UHDTV2": Size(7680, 4320),
}

__all__ = ["SIZES", "Size", "__version__"]
