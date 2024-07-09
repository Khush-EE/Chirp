import json
from home.models import ChatModel, UserModel
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
class ChatConsumer(WebsocketConsumer):

    sender = None
    reciever = None
    count = 0

    def connect(self):

        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.group_name = f"chat_{self.room_name}"

        async_to_sync(self.channel_layer.group_add)(self.group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        print(close_code)
        async_to_sync(self.channel_layer.group_discard)(self.group_name, self.channel_name)


    def receive(self, text_data):
        chatDataJson = json.loads(text_data)
        senderUsername = chatDataJson['sender']
        recieverUsername = chatDataJson['reciever']
        message = chatDataJson['message']

        if self.sender is None:
            self.sender = UserModel.objects.get(username=senderUsername)
            self.reciever = UserModel.objects.get(username=recieverUsername)

        ChatModel.objects.create(sender=self.sender, reciever=self.reciever, message=message)

        async_to_sync(self.channel_layer.group_send)(
            self.group_name,
            {
                'type': 'chat_message',
                'sender': senderUsername,
                'reciever': recieverUsername,
                'message': message
            }
        )

    def chat_message(self, event):

        self.send(json.dumps({
            "sender": event['sender'],
            "reciever": event['reciever'],
            "message": event['message']
        }));

        # pass