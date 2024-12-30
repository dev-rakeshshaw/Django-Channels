from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer
from asgiref.sync import async_to_sync

# Synchronous WebSocket consumer class
class MySyncConsumer(SyncConsumer):
    # Method to handle WebSocket connection establishment
    def websocket_connect(self, event):
        # Log the connection event
        print("WebSocket connection established with the client.", event)
        
        # Retrieve the channel layer instance (for managing communication between consumers)
        print("Channel Layer......", self.channel_layer)
        
        # Retrieve the unique channel name for this WebSocket connection
        print("Channel Name......", self.channel_name)
        
        # Add this channel to a group named 'programmers'
        # Allows broadcasting messages to all WebSocket connections in the group
        async_to_sync(self.channel_layer.group_add)("programmers", self.channel_name)
        
        # Send a WebSocket accept message to acknowledge the connection
        self.send({
            'type': 'websocket.accept'
        })

    # Method to handle messages received from the WebSocket client
    def websocket_receive(self, event):
        # Log the message received from the client
        print(f"Message received from client: {event['text']}")
        
        # Send the received message to the group named 'programmers'
        async_to_sync(self.channel_layer.group_send)(
            'programmers',  # Group name
            {
                'type': 'chat.message',  # Event type handled by the `chat_message` method
                'message': event['text']  # The actual message content
            }
        )

    # Method to handle messages broadcasted to the group
    def chat_message(self, event):
        # Log the event data received
        print("Event......", event)
        print("Actual Data......", event["message"])
        
        # Send the broadcasted message back to the WebSocket client
        self.send({
            'type': 'websocket.send',  # WebSocket send message type
            'text': event['message']  # Message content
        })

    # Method to handle WebSocket disconnection
    def websocket_disconnect(self, event):
        # Log the disconnection event
        print("WebSocket connection closed by the client.", event)
        
        # Retrieve the channel layer instance
        print("Channel Layer......", self.channel_layer)
        
        # Retrieve the unique channel name for this WebSocket connection
        print("Channel Name......", self.channel_name)
        
        # Remove this channel from the group named 'programmers'
        async_to_sync(self.channel_layer.group_discard)("programmers", self.channel_name)
        
        # Raise StopConsumer to clean up and stop the consumer
        raise StopConsumer()



# Synchronous WebSocket consumer class
class MyAsyncConsumer(AsyncConsumer):
    # Method to handle WebSocket connection establishment
    async def websocket_connect(self, event):
        # Log the connection event
        print("WebSocket connection established with the client.", event)
        
        # Retrieve the channel layer instance (for managing communication between consumers)
        print("Channel Layer......", self.channel_layer)
        
        # Retrieve the unique channel name for this WebSocket connection
        print("Channel Name......", self.channel_name)
        
        self.group_name = self.scope['url_route']['kwargs']['group_name']

        print("group_name----------->",self.group_name)
        # Add this channel to a group named 'programmers'
        # Allows broadcasting messages to all WebSocket connections in the group
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        
        # Send a WebSocket accept message to acknowledge the connection
        await self.send({
            'type': 'websocket.accept'
        })

    # Method to handle messages received from the WebSocket client
    async def websocket_receive(self, event):
        # Log the message received from the client
        print(f"Message received from client: {event['text']}")
        
        # Send the received message to the group named 'programmers'
        await self.channel_layer.group_send(
            self.group_name,  # Group name
            {
                'type': 'chat.message',  # Event type handled by the `chat_message` method
                'message': event['text']  # The actual message content
            }
        )

    # Method to handle messages broadcasted to the group
    async def chat_message(self, event):
        # Log the event data received
        print("Event......", event)
        print("Actual Data......", event["message"])
        
        # Send the broadcasted message back to the WebSocket client
        await self.send({
            'type': 'websocket.send',  # WebSocket send message type
            'text': event['message']  # Message content
        })

    # Method to handle WebSocket disconnection
    async def websocket_disconnect(self, event):
        # Log the disconnection event
        print("WebSocket connection closed by the client.", event)
        
        # Retrieve the channel layer instance
        print("Channel Layer......", self.channel_layer)
        
        # Retrieve the unique channel name for this WebSocket connection
        print("Channel Name......", self.channel_name)
        
        # Remove this channel from the group named 'programmers'
        await self.channel_layer.group_discard(self.group_name, self.channel_name)
        
        # Raise StopConsumer to clean up and stop the consumer
        raise StopConsumer()