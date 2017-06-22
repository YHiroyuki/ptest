# -*- coding: utf-8 -*-
import pytest

from csv_validater.load_file import read_lines_by_file_path


def describe_read_lines_by_files():

    def test_utf8_file():
        file_path = "./tests/load_file/data/sample_utf8_file.csv"
        result = read_lines_by_file_path(file_path)
        assert result


    def when_shift_jis_file():
        pass

    def test_not_exists_file():
        file_path = "./tests/load_file/data/sample_not_exists_file.csv"
        with pytest.raises(FileNotFoundError):
            read_lines_by_file_path(file_path)
