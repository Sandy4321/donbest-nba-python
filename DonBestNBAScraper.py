from datetime import date, timedelta
import httplib2
import json
import logging
import os
from urllib import urlencode

class DonBestNBAScraper:

  def __init__(self,**kwargs):

      # pass in handler on instantiation
      if 'handler' in kwargs:
          self.handler = kwargs['handler']
      else:
          self.handler = httplib2.Http(".cache")

      if 'logger' in kwargs:
          self.logger = kwargs['logger']
      else:
          self.logger = logging.getLogger(__name__)

      if 'dldir' in kwargs:
          self.dldir = kwargs['dldir']
      else:
          self.dldir = '/home/sansbacon/workspace/donbest-nba-python/data'

    def odds(self, gamedate):

        odds_page = None
        base_url = 'http://www.donbest.com/nba/odds/'
        url = "{0}{1}.html".format(base_url, gamedate)
        self.logger.debug(url)

        # NOT IMPLEMENTED
        # get the content from a file, if exists
        #fn = os.path.join(self.dldir, )
        #content = self._get_from_file(fn)
        content = None

        # FILE SAVING NOT IMPLEMENTED
        # if not in a file, then get from the web and save it
        if not content:
            self.logger.debug('getting from web: ' + url)
            #content = self._get_from_web(url,fn)
            content = self._get_from_web(url)

            # if not from web either, then log an error
            if not content:
                self.logger.error('could not get content from file or url\n' + fn + '\n' + url)

        else:
            self.logger.debug('got from file: ' + fn)

        return content, url
     
    ### start "private" methods

    def _get_from_file(self, fn):
        # content is none if file does not exist
        content = None

        # test if file exists, if so, slurp it into content
        if os.path.isfile(fn):
            self.logger.debug(fn)

            try:
                with open(fn) as x:
                    content = x.read()

            except:
                self.logger.exception('could not read from file ' + fn)

        return content

    def _get_from_web(self, url, fn=None):
        # content is none if file can't be downloaded
        content = None

        # try to download, if successful, then save file
        try:
            (resp, body) = self.handler.request(url, "GET")
            self.logger.debug('got content from web')

        except:
            self.logger.exception('could not get from web ' + url)

        # want to make sure that get the correct content, so check request status before returning content
        if resp.status == 200:
            content = body

        # save content to a file if fn passed as parameter
        if fn:
            try:
                with open(fn, 'w') as outfile:
                    outfile.write(content)
            except:
                self.logger.exception('could not save file ' + fn)

        # if wrong, then log the actual message, content value is still None
        else:
            self.logger.error('http request error ' + resp.status + "\n" + body)

        # ship it
        return content

if __name__ == "__main__":
  pass
