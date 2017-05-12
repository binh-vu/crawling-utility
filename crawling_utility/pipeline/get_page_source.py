#!/usr/bin/python
# -*- coding: utf-8 -*-

from crawling_utility.base import Pipe


class GetPageSource(Pipe):
    def run(self, data):
        data.content = data.driver.page_source
        return data
