# Embedded file name: /home/oe1/atv64arm/build-enviroment/builds/openatv/release/hd60/tmp/work/cortexa15hf-neon-vfpv4-oe-linux-gnueabi/enigma2-plugin-skins-madmax-impossible/1.6+gitAUTOINC+1b553b6778-r0/git/MadMax-Impossible-Skin/usr/lib/enigma2/python/Components/Converter/MMRouteInfo.py
from Components.Converter.Converter import Converter
from Components.Element import cached

class MMRouteInfo(Converter, object):
    Info = 0
    Lan = 1
    Wifi = 2
    Modem = 3

    def __init__(self, type):
        Converter.__init__(self, type)
        if type == 'Info':
            self.type = self.Info
        elif type == 'Lan':
            self.type = self.Lan
        elif type == 'Wifi':
            self.type = self.Wifi
        elif type == 'Modem':
            self.type = self.Modem

    @cached
    def getBoolean(self):
        info = False
        for line in open('/proc/net/route'):
            if self.type == self.Lan and line.split()[0] == 'eth0' and line.split()[3] == '0003':
                info = True
            elif self.type == self.Wifi and (line.split()[0] == 'wlan0' or line.split()[0] == 'ra0') and line.split()[3] == '0003':
                info = True
            elif self.type == self.Modem and line.split()[0] == 'ppp0' and line.split()[3] == '0003':
                info = True

        return info

    boolean = property(getBoolean)

    @cached
    def getText(self):
        info = ''
        for line in open('/proc/net/route'):
            if self.type == self.Info and line.split()[0] == 'eth0' and line.split()[3] == '0003':
                info = 'lan'
            elif self.type == self.Info and (line.split()[0] == 'wlan0' or line.split()[0] == 'ra0') and line.split()[3] == '0003':
                info = 'wifi'
            elif self.type == self.Info and line.split()[0] == 'ppp0' and line.split()[3] == '0003':
                info = '3g'

        return info

    text = property(getText)

    def changed(self, what):
        Converter.changed(self, what)