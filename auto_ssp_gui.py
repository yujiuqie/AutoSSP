#coding=utf-8

#Created by Alfred Jiang 20160523

import rumps
import auto_ssp

class AwesomeStatusBarApp(rumps.App):
    @rumps.clicked("Service A")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_a_section()

    @rumps.clicked("Service B")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_b_section()

    @rumps.clicked("Service C")
    def onoff(self, sender):
        # sender.state = not sender.state
        auto_ssp.fetch_c_section()

if __name__ == "__main__":
    AwesomeStatusBarApp("FFS").run()