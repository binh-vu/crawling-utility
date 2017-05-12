#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from crawling_utility.base import Pipe, PipeObject


class GetURL(Pipe):

    def run(self, data: PipeObject) -> PipeObject:
        r = requests.get(data.url)

        data.file_content = r.text
        data.content = r.text

        return data
