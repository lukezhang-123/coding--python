"""
python 查看windows系统剪贴板格式和内容
"""

# src: https://gist.github.com/Rhomboid/5155189

import win32clipboard


def print_clipboard_fmt():
    """
    查看系统剪贴板格式，识别正确的格式才能获取到正确内容
    :return:
    """
    formats = {val: name for name, val in vars(win32clipboard).items() if name.startswith('CF_')}

    def format_name(fmt):
        """
        查找剪贴板格式代码和名称
        :param fmt: 剪贴板格式代码, int
        :return: 格式list, 每一个object为：格式代码(格式名称)
        """
        if fmt in formats:
            return formats[fmt]  # 查找win32clipboard包内预定义的格式名称, CF_开头
        try:
            return win32clipboard.GetClipboardFormatName(fmt)  # 查找系统支持的格式名称
        except Exception:
            return "unknown"

    win32clipboard.OpenClipboard(None)
    fmt_list = []
    fmt = 0
    while True:
        fmt = win32clipboard.EnumClipboardFormats(fmt)
        if fmt == 0:
            break
        # print('{:5} ({})'.format(fmt, format_name(fmt)))
        fmt_list.append('{:5} ({})'.format(fmt, format_name(fmt)))
    win32clipboard.CloseClipboard()
    return fmt_list


# for debug
print(print_clipboard_fmt())

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData(49344)  # 49344 (HTML Format), 复制网页文字，保留了格式
win32clipboard.CloseClipboard()
print(data.decode())
