from gendiff.formatters import stylish_format, plain_format, normalize


FORMATS = {
    "stylish": stylish_format,
    "plain": plain_format,
}


def formatt(tree, format_):
    if format_ not in FORMATS:
        raise ValueError('Unsupported format. Next formats are supported: {}'
                         .format(FORMATS.keys()))
    return FORMATS[format_].format(tree)