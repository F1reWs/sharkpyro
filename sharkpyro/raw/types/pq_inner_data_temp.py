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


class PQInnerDataTemp(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.PQInnerData`.

    Details:
        - Layer: ``139``
        - ID: ``0x3c6a84d4``

    Parameters:
        pq: ``bytes``
        p: ``bytes``
        q: ``bytes``
        nonce: ``int`` ``128-bit``
        server_nonce: ``int`` ``128-bit``
        new_nonce: ``int`` ``256-bit``
        expires_in: ``int`` ``32-bit``
    """

    __slots__: List[str] = ["pq", "p", "q", "nonce", "server_nonce", "new_nonce", "expires_in"]

    ID = 0x3c6a84d4
    QUALNAME = "types.PQInnerDataTemp"

    def __init__(self, *, pq: bytes, p: bytes, q: bytes, nonce: int, server_nonce: int, new_nonce: int, expires_in: int) -> None:
        self.pq = pq  # bytes
        self.p = p  # bytes
        self.q = q  # bytes
        self.nonce = nonce  # int128
        self.server_nonce = server_nonce  # int128
        self.new_nonce = new_nonce  # int256
        self.expires_in = expires_in  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PQInnerDataTemp":
        # No flags
        
        pq = Bytes.read(b)
        
        p = Bytes.read(b)
        
        q = Bytes.read(b)
        
        nonce = Int128.read(b)
        
        server_nonce = Int128.read(b)
        
        new_nonce = Int256.read(b)
        
        expires_in = Int.read(b)
        
        return PQInnerDataTemp(pq=pq, p=p, q=q, nonce=nonce, server_nonce=server_nonce, new_nonce=new_nonce, expires_in=expires_in)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.pq))
        
        b.write(Bytes(self.p))
        
        b.write(Bytes(self.q))
        
        b.write(Int128(self.nonce))
        
        b.write(Int128(self.server_nonce))
        
        b.write(Int256(self.new_nonce))
        
        b.write(Int(self.expires_in))
        
        return b.getvalue()
