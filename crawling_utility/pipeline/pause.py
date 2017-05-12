#!/usr/bin/python
# -*- coding: utf-8 -*-

from crawling_utility.base import Pipe


class KeyboardResume(Pipe):
    def run(self, data):
        input('Enter to continue...')
        return data
