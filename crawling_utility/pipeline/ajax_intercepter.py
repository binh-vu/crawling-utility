#!/usr/bin/python
# -*- coding: utf-8 -*-

import uuid

from crawling_utility.base import Pipe, PipeObject

intercepter = '''
(function() {
    'use strict';

    var element = document.createElement('div');
    element.id = '{element_id}';

    document.body.appendChild(element);

    $(document).ajaxSuccess(function(event, xhr, settings) {
        var result = document.createElement('p');

        $(result).text(JSON.stringify({
            response: xhr.responseText,
            requestURL: settings.url
        }));

        element.appendChild(result);
    });
})()
'''


class AjaxIntercepter(Pipe):

    def __init__(self, load_every_time: bool):
        """
        :param load_every_time: load the intercepter script every time (using when loading new page)
        """
        self.element_id = str(uuid.uuid4()) + '-intercepter'
        self.load_every_time = load_every_time
        self.load_intercept_first_time = False

    def run(self, data: PipeObject) -> PipeObject:
        data.element_id = self.element_id

        if self.load_every_time:
            data.driver.execute_script(intercepter.replace('{element_id}', self.element_id))
        else:
            if not self.load_intercept_first_time:
                data.driver.execute_script(intercepter.replace('{element_id}', self.element_id))

        if not self.load_intercept_first_time:
            self.load_intercept_first_time = True

        return data
