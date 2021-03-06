# -*- coding: utf-8 -*-
"""Error controller"""

from tg import request, expose

__all__ = ['ErrorController']


error_cats = {
    403: {'img': 'http://farm8.staticflickr.com/7173/6508023617_f3ffc34e17_b.jpg',
          'a': 'http://www.flickr.com/photos/girliemac/6508023617/'},
    404: {'img': 'http://farm8.staticflickr.com/7172/6508022985_b22200ced0_b.jpg',
          'a': 'http://www.flickr.com/photos/girliemac/6508022985/'},
    500: {'img': 'http://farm8.staticflickr.com/7001/6509400855_f36a7fea54_o.jpg',
          'a': 'http://www.flickr.com/photos/girliemac/6509400855/'},
}


class ErrorController(object):
    """
    Generates error documents as and when they are required.

    The ErrorDocuments middleware forwards to ErrorController when error
    related status codes are returned from the application.

    This behaviour can be altered by changing the parameters to the
    ErrorDocuments middleware in your config/middleware.py file.

    """

    @expose('errorcats.templates.error')
    def document(self, *args, **kwargs):
        """Render the error document"""
        resp = request.environ.get('pylons.original_response')
        code = request.params.get('code', resp.status_int)
        error = error_cats[code]
        message = ('')
        return dict(img=error['img'], link=error['a'], code=code,
                    message=message)
