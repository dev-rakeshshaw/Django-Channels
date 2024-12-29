from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from time import sleep
import asyncio

class MySyncConsumer(SyncConsumer):
    # Handles WebSocket connection for synchronous communication
    def websocket_connect(self, event):
        print("WebSocket connection established with the client.", event)
        self.send({
            'type': 'websocket.accept'  # Accepting the WebSocket connection
        })

    def websocket_receive(self, event):
        # Logs the message received from the client
        print(f"Message received from client: {event.get('text', 'No message received')}")
        
        # Sends multiple replies back to the client
        for i in range(50):
            self.send({
                'type': 'websocket.send',
                'text': f"Replying to client: message number {i}"
            })
            sleep(1)  # Simulate a delay between messages

    def websocket_disconnect(self, event):
        # Logs disconnection events
        print("WebSocket connection closed by the client.", event)
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    # Handles WebSocket connection for asynchronous communication
    async def websocket_connect(self, event):
        print("WebSocket connection established with the client.", event)
        await self.send({
            'type': 'websocket.accept'  # Accepting the WebSocket connection
        })

    async def websocket_receive(self, event):
        # Logs the message received from the client
        print(f"Message received from client: {event.get('text', 'No message received')}")
        
        # Sends multiple replies back to the client asynchronously
        for i in range(50):
            await self.send({
                'type': 'websocket.send',
                'text': f"Replying to client: message number {i}"
            })
            await asyncio.sleep(1)  # Simulate a delay between messages

    async def websocket_disconnect(self, event):
        # Logs disconnection events
        print("WebSocket connection closed by the client.", event)
        raise StopConsumer()
