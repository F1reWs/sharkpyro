#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Union, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageReactionsList(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.messages.MessageReactionsList`.

    Details:
        - Layer: ``139``
        - ID: ``0x31bd492d``

    Parameters:
        count: ``int`` ``32-bit``
        reactions: List of :obj:`MessagePeerReaction <pyrogram.raw.base.MessagePeerReaction>`
        chats: List of :obj:`Chat <pyrogram.raw.base.Chat>`
        users: List of :obj:`User <pyrogram.raw.base.User>`
        next_offset (optional): ``str``

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`messages.GetMessageReactionsList <pyrogram.raw.functions.messages.GetMessageReactionsList>`
    """

    __slots__: List[str] = ["count", "reactions", "chats", "users", "next_offset"]

    ID = 0x31bd492d
    QUALNAME = "types.messages.MessageReactionsList"

    def __init__(self, *, count: int, reactions: List["raw.base.MessagePeerReaction"], chats: List["raw.base.Chat"], users: List["raw.base.User"], next_offset: Union[None, str] = None) -> None:
        self.count = count  # int
        self.reactions = reactions  # Vector<MessagePeerReaction>
        self.chats = chats  # Vector<Chat>
        self.users = users  # Vector<User>
        self.next_offset = next_offset  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageReactionsList":
        flags = Int.read(b)
        
        count = Int.read(b)
        
        reactions = TLObject.read(b)
        
        chats = TLObject.read(b)
        
        users = TLObject.read(b)
        
        next_offset = String.read(b) if flags & (1 << 0) else None
        return MessageReactionsList(count=count, reactions=reactions, chats=chats, users=users, next_offset=next_offset)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.next_offset is not None else 0
        b.write(Int(flags))
        
        b.write(Int(self.count))
        
        b.write(Vector(self.reactions))
        
        b.write(Vector(self.chats))
        
        b.write(Vector(self.users))
        
        if self.next_offset is not None:
            b.write(String(self.next_offset))
        
        return b.getvalue()
