#!/usr/bin/python

import urllib2

class GoPro:
    PASSWORD = 'keverngopro'
    URL = 'http://10.5.5.9/'
    IMAGE_PAGE = 'videos/DCIM/100GOPRO/'
    IMAGE_FORMAT = 'GOPR{:0>4}.JPG'

    _currentFile = 0;

    def __init__(self):
        self._cameraMode()
        self._findLastImage()

    def shutter(self):
        GoPro._currentFile += 1

        cmd = 'bacpac/SH?t=' + GoPro.PASSWORD + '&p=%01'
        self._hit(cmd)

    def getLastImage(self):
        cmd = self._lastImageURL()
        filename = self._lastImageName()
        self._download(cmd, filename)

        return filename

    def _cameraMode(self):
        cmd = 'camera/CM?t=' + GoPro.PASSWORD + '&p=%01'
        self._hit(cmd)

    def _hit(self, path):
        return urllib2.urlopen(GoPro.URL + path)

    def _download(self, path, filename):
        response = self._hit(path)

        with open('images/' + filename, "wb") as img:
            img.write(response.read())

    def _lastImageURL(self):
        return GoPro.IMAGE_PAGE + self._lastImageName() 

    def _lastImageName(self):
        return GoPro.IMAGE_FORMAT.format(GoPro._currentFile)

    def _findLastImage(self):
        GoPro._currentFile = 0

        error = True
        while error:
            GoPro._currentFile += 1

            try:
                self._hit(self._lastImageURL())
                error = False
            except (urllib2.HTTPError, urllib2.URLError), e:
                pass

        error = False
        while not error:
            GoPro._currentFile += 1

            try:
                self._hit(self._lastImageURL())
            except (urllib2.HTTPError, urllib2.URLError), e:
                error = True

        GoPro._currentFile -= 1
