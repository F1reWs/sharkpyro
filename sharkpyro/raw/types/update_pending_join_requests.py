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


class UpdatePendingJoinRequests(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``139``
        - ID: ``0x7063c3db``

    Parameters:
        peer: :obj:`Peer <pyrogram.raw.base.Peer>`
        requests_pending: ``int`` ``32-bit``
        recent_requesters: List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["peer", "requests_pending", "recent_requesters"]

    ID = 0x7063c3db
    QUALNAME = "types.UpdatePendingJoinRequests"

    def __init__(self, *, peer: "raw.base.Peer", requests_pending: int, recent_requesters: List[int]) -> None:
        self.peer = peer  # Peer
        self.requests_pending = requests_pending  # int
        self.recent_requesters = recent_requesters  # Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdatePendingJoinRequests":
        # No flags
        
        peer = TLObject.read(b)
        
        requests_pending = Int.read(b)
        
        recent_requesters = TLObject.read(b, Long)
        
        return UpdatePendingJoinRequests(peer=peer, requests_pending=requests_pending, recent_requesters=recent_requesters)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.requests_pending))
        
        b.write(Vector(self.recent_requesters, Long))
        
        return b.getvalue()
