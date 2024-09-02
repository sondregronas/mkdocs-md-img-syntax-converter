from importlib.metadata import version, PackageNotFoundError

from md_img_syntax_converter.plugin import MdImgSyntaxConverterPlugin  # noqa: F401

try:
    __version__ = version("md-img-syntax-converter")
except PackageNotFoundError:  # pragma: no cover
    # package is not installed
    pass
