#coding=utf-8

#Created by Alfred Jiang 20160523

import rumps
import auto_ssp

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked(u"免费 A 服务器")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_a_section()

    @rumps.clicked(u"免费 B 服务器")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_b_section()

    @rumps.clicked(u"免费 C 服务器")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_c_section()

if __name__ == "__main__":
    AwesomeStatusBarApp("FFS").run()