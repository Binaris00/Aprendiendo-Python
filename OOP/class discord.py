"""
Program about discord basic things and topics
"""

class Discord_server:
    def __init__(self, name, image, chats, perms, members, emoji, stickers) -> None:
        self.name = name
        self.image = None
        self.chats = chats
        self.perms = perms
        self.members = []
        self.emoji = emoji
        self.stickers = stickers
    
    def set_name(self, new_name):
        self.name = new_name
        return f"The new discord server name is: {self.name}"
    
    def set_image(self, new_image):
        self.name = new_image
        return f"The new discord server name is: {self.name}"
    
    def new_member(self, new_member):
        pass