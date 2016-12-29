import asyncio
import sys
from asynccmd import Cmd

class SimpleCommander(Cmd):
    def __init__(self, mode, intro, prompt):
        super().__init__(mode=mode) # We need to pass in Cmd class mode of async cmd running
        self.intro = intro
        self.prompt = prompt
        self.loop = None

    def do_tasks(self, arg):
        """
        Our example method. Type "tasks <arg>"
        :param arg: contain args that go after command
        :return: None
        """
        for task in asyncio.Task.all_tasks(loop=self.loop):
            print(task)

    def start(self, loop=None):
        self.loop = loop # We pass our loop to Cmd class. If None it try to get default asyncio loop.
        super().cmdloop(loop) # Create async tasks to run in loop. There is run_loop=false by default

# For win system we have only Run mode
# For POSIX system Reader mode is preferred
if sys.platform == 'win32':
   loop = asyncio.ProactorEventLoop()
   mode = "Run"
else:
   loop = asyncio.get_event_loop()
   mode = "Reader"
cmd = SimpleCommander(mode=mode, intro="This is example", prompt="example> ") #create instanse
cmd.start(loop) #prepaire instance
try:
    loop.run_forever() # our cmd will run automatilly from this moment
except KeyboardInterrupt:
    loop.stop()
