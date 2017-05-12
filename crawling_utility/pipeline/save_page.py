#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from pyutils.hash import md5
from slugify import slugify

from crawling_utility.base import Pipe, PipeObject


class SavePage(Pipe):

    def __init__(self, save_dir: str):
        self.save_dir = save_dir
        assert os.path.exists(self.save_dir), '%s doesn\'t exist' % self.save_dir

    def get_file_name(self, url: str) -> str:
        return '%s-%s.html' % (md5(url), slugify(url))

    def run(self, data: PipeObject) -> PipeObject:
        file_name = self.get_file_name(data.url)
        file_path = os.path.join(self.save_dir, file_name)

        with open(file_path, 'w') as f:
            f.write(data.content)

        data.file_name = file_name
        return data
