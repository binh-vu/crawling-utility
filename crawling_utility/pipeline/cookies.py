#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

import pickle

from crawling_utility.base import Pipe, PipeObject


class SaveCookies(Pipe):
    def __init__(self, save_dir: str, cookie_name: str = None) -> None:
        self.save_dir: str = save_dir
        self.cookie_name: str = 'default' if cookie_name is None else cookie_name

        assert os.path.exists(self.save_dir), '%s doesn\'t exist' % self.save_dir

    def run(self, data: PipeObject) -> PipeObject:
        assert 'driver' in data, 'Need selenium driver'

        with open(os.path.join(self.save_dir, f'cookies_{self.cookie_name}'), 'w') as f:
            pickle.dump(data.driver.get_cookies(), f)
        return data


class LoadCookies(Pipe):
    def __init__(self, save_dir: str, domain: str, cookie_name: str = None) -> None:
        self.save_dir: str = save_dir
        self.domain: str = domain
        self.cookie_name: str = 'default' if cookie_name is None else cookie_name

        assert os.path.exists(self.save_dir), '%s doesn\'t exist' % self.save_dir

    def run(self, data: PipeObject) -> PipeObject:
        with open(os.path.join(self.save_dir, f'cookies_{self.cookie_name}'), 'w') as f:
            cookies = pickle.load(f)

        for cookie in cookies:
            if cookie['domain'].find(self.domain) != -1:
                data.driver.add_cookie(cookie)

        return data
