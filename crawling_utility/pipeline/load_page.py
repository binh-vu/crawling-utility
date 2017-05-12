#!/usr/bin/python
# -*- coding: utf-8 -*-

from crawling_utility.base import Pipe, PipeObject


class LoadPage(Pipe):

    def run(self, data: PipeObject) -> PipeObject:
        assert 'driver' in data, 'Need selenium driver'
        data.driver.get(data.url)
        return data
