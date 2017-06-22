# -*- coding: utf-8 -*-
import csv

from csv_validater import errors


def read_lines_by_file_path(file_path):
    """ ファイルパスからUTF-8 Shift-jisのファイルを読み込む
    Args:
        file_path: 読み込むファイルパス
    Returns:
        ファイルの行リスト
    """
    codecs = ('utf_8_sig', 'shift-jis')
    f = None
    try:
        for codec in codecs:
            f = open(file_path, encoding=codec)
            try:
                lines = f.readlines()
                return lines
            except UnicodeDecodeError:
                f.close()
        raise errors.FileOpenError("File not opened", file_path)
    finally:
        if f is not None:
            f.close()
