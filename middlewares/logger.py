# created by sangeet verma for project falcon_basics
# on 12/11/17 :: 8:00 PM

import logging
from datetime import datetime
from setup import production

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG,
                    filename='logs/production',
                    datefmt='%m-%d %H:%M',
                    filemode='a')


class ResponseLoggerMiddleware(object):
    def process_response(self, req, resp, resource, req_succeeded):
        if production:
            st = '{0} {1} {2} {3} {4} {5}'.format(
                datetime.utcnow(),
                req.remote_addr,
                req.method,
                req.relative_uri,
                resp.status[:3],
                resp.body
            )
            logger.debug(st)
        else:
            st = '{0} {1} {2} {3} {4} {5} {6}'.format(
                datetime.utcnow(),
                req.remote_addr,
                req.method,
                req.relative_uri,
                resp.status[:3],
                req.query_string,
                resp.body
            )
            print(st)
