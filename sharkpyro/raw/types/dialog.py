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


class Dialog(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Dialog`.

    Details:
        - Layer: ``139``
        - ID: ``0xa8edd0f5``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        top_message: ``int`` ``32-bit``
        read_inbox_max_id: ``int`` ``32-bit``
        read_outbox_max_id: ``int`` ``32-bit``
        unread_count: ``int`` ``32-bit``
        unread_mentions_count: ``int`` ``32-bit``
        unread_reactions_count: ``int`` ``32-bit``
        notify_settings: :obj:`PeerNotifySettings <pyrogram.raw.base.PeerNotifySettings>`
        pinned (optional): ``bool``
        unread_mark (optional): ``bool``
        pts (optional): ``int`` ``32-bit``
        draft (optional): :obj:`DraftMessage <pyrogram.raw.base.DraftMessage>`
        folder_id (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["peer", "top_message", "read_inbox_max_id", "read_outbox_max_id", "unread_count", "unread_mentions_count", "unread_reactions_count", "notify_settings", "pinned", "unread_mark", "pts", "draft", "folder_id"]

    ID = 0xa8edd0f5
    QUALNAME = "types.Dialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, read_inbox_max_id: int, read_outbox_max_id: int, unread_count: int, unread_mentions_count: int, unread_reactions_count: int, notify_settings: "raw.base.PeerNotifySettings", pinned: Union[None, bool] = None, unread_mark: Union[None, bool] = None, pts: Union[None, int] = None, draft: "raw.base.DraftMessage" = None, folder_id: Union[None, int] = None) -> None:
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.read_inbox_max_id = read_inbox_max_id  # int
        self.read_outbox_max_id = read_outbox_max_id  # int
        self.unread_count = unread_count  # int
        self.unread_mentions_count = unread_mentions_count  # int
        self.unread_reactions_count = unread_reactions_count  # int
        self.notify_settings = notify_settings  # PeerNotifySettings
        self.pinned = pinned  # flags.2?true
        self.unread_mark = unread_mark  # flags.3?true
        self.pts = pts  # flags.0?int
        self.draft = draft  # flags.1?DraftMessage
        self.folder_id = folder_id  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Dialog":
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        unread_mark = True if flags & (1 << 3) else False
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        read_inbox_max_id = Int.read(b)
        
        read_outbox_max_id = Int.read(b)
        
        unread_count = Int.read(b)
        
        unread_mentions_count = Int.read(b)
        
        unread_reactions_count = Int.read(b)
        
        notify_settings = TLObject.read(b)
        
        pts = Int.read(b) if flags & (1 << 0) else None
        draft = TLObject.read(b) if flags & (1 << 1) else None
        
        folder_id = Int.read(b) if flags & (1 << 4) else None
        return Dialog(peer=peer, top_message=top_message, read_inbox_max_id=read_inbox_max_id, read_outbox_max_id=read_outbox_max_id, unread_count=unread_count, unread_mentions_count=unread_mentions_count, unread_reactions_count=unread_reactions_count, notify_settings=notify_settings, pinned=pinned, unread_mark=unread_mark, pts=pts, draft=draft, folder_id=folder_id)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        flags |= (1 << 3) if self.unread_mark else 0
        flags |= (1 << 0) if self.pts is not None else 0
        flags |= (1 << 1) if self.draft is not None else 0
        flags |= (1 << 4) if self.folder_id is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        b.write(Int(self.read_inbox_max_id))
        
        b.write(Int(self.read_outbox_max_id))
        
        b.write(Int(self.unread_count))
        
        b.write(Int(self.unread_mentions_count))
        
        b.write(Int(self.unread_reactions_count))
        
        b.write(self.notify_settings.write())
        
        if self.pts is not None:
            b.write(Int(self.pts))
        
        if self.draft is not None:
            b.write(self.draft.write())
        
        if self.folder_id is not None:
            b.write(Int(self.folder_id))
        
        return b.getvalue()
