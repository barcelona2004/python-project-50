from gendiff.formatters import stylish_format, plain_format, json_format

FORMATS = {
    "stylish": stylish_format,
    "plain": plain_format,
    "json": json_format
}


def formatt(tree, f):
    if f not in FORMATS:
        raise ValueError('Unsupported format.'
                         'Next formats are supported: {}'
                         .format(FORMATS.keys()))
    return FORMATS[f].format(tree)
