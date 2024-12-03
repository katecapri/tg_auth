import json
from time import sleep
from channels.generic.websocket import WebsocketConsumer
import logging
from link.models import User

logger = logging.getLogger('app')

class WSConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()
        token = self.scope['url_route']['kwargs']['token']
        user = None
        while user is None:
            user = User.objects.filter(token=token).first()
            if user:
                self.send(json.dumps({'message': user.name}))
            else:
                sleep(5)
        self.close()

