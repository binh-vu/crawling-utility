#!/usr/bin/python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

from crawling_utility.base import Pipe


class VirtualDOM(Pipe):
    def __init__(self):
        super(VirtualDOM, self).__init__()

    def read_from_file(self, file_path: str) -> str:
        with open(file_path, 'rb') as f:
            return f.read().decode()

    def run(self, data):
        if 'file_content' in data:
            html = data.file_content
        else:
            html = self.read_from_file(data.file_path)

        data._: BeautifulSoup = BeautifulSoup(html, 'html.parser')
        return data
