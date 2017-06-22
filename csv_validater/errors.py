# -*- coding: utf-8 -*-

class Error(Exception):
    """ 共通エラー """
    # TODO console: 検証エラー(err_msg), e.log: エラーのスタックトレース
    def __init__(self, err_msg, **kwargs):
        super(Error, self).__init__(err_msg)


class FileOpenError(Error):

    def __init__(self, err_msg, file_path, **kwargs):
        super(FileOpenError, self).__init__(err_msg)
