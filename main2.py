"""
An example client that joins any rooms that its specified owner does.
"""
import showdown
from showdown import Room
import logging
from showdown.utils import strip_prefix

room_id_user = ""

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with open("./login.txt", "rt") as f, open("./owner.txt", "rt") as o:
    username, password = f.read().strip().splitlines()
    ownername = o.read().strip()


class FollowerClient(showdown.Client):
    def __init__(self, **kwargs):
        self.room_id = ""
        self.check_ou()
        showdown.Client.__init__(self, **kwargs)
        self.owner = showdown.User(ownername, client=self)

    async def on_query_response(self, response_type, data):
        if response_type == "userdetails":
            global room_id_user
            self.room_id = list(data.get("rooms").keys())[1][1:]
            await self.join(self.room_id)


    @showdown.Client.on_interval(interval=3)
    async def get_owner_details(self):
        await self.owner.request_user_details()

    async def on_receive(self, room_id, inp_type, params):
        if room_id == self.room_id and room_id != "":
            print('\n'.join(self.rooms[room_id].logs))

    @showdown.Client.on_interval(interval=3)
    async def check_ou(self):
        await self.query_battles('gen9ou', lifespan=3)


FollowerClient(name=username, password=password).start()