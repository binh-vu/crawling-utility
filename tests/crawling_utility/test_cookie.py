#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from nose.tools import ok_

from crawling_utility.base import Pipeline
from crawling_utility.pipeline import ChromeDriver, LoadPage, GetPageSource, SaveCookies, LoadCookies


def test_save_and_load_cookie():
    with ChromeDriver() as se_driver:
        pipeline = Pipeline()
        pipeline.add_pipe(se_driver)
        pipeline.add_pipe(LoadPage())
        pipeline.add_pipe(GetPageSource())
        pipeline.add_pipe(SaveCookies(save_dir='/tmp', cookie_name='test'))

        pipeline.run(url='http://vnexpress.net')
        ok_(os.path.exists('/tmp/cookies_test'))

        pipeline = Pipeline()
        pipeline.add_pipe(se_driver)
        pipeline.add_pipe(LoadPage())
        pipeline.add_pipe(GetPageSource())
        pipeline.add_pipe(LoadCookies(save_dir='/tmp', domain='vnexpress.net', cookie_name='test'))

        pipeline.run(url='http://vnexpress.net')
