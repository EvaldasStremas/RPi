"""
https://pypi.org/project/telnetsrv/
"""

import gevent, gevent.server
from telnetsrv.green import TelnetHandler, command

class MyTelnetHandler(TelnetHandler):
    WELCOME = "Welcome to my server."

    @command(['echo', 'copy', 'repeat'])
    def command_echo(self, params):
        '''<text to echo>
        Echo text back to the console.

        '''
        self.writeresponse( ' '.join(params) )

    @command('timer')
    def command_timer(self, params):
        '''<time> <message>
        In <time> seconds, display <message>.
        Send a message after a delay.
        <time> is in seconds.
        If <message> is more than one word, quotes are required.
        example:
        > TIMER 5 "hello world!"
        '''
        try:
            timestr, message = params[:2]
            time = int(timestr)
        except ValueError:
            self.writeerror( "Need both a time and a message" )
            return
        self.writeresponse("Waiting %d seconds...", time)
        gevent.spawn_later(time, self.writemessage, message)


server = gevent.server.StreamServer(("", 8023), MyTelnetHandler.streamserver_handle)
server.serve_forever()