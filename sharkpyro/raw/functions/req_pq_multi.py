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


class ReqPqMulti(TLObject):  # type: ignore
    """Telegram API method.

    Details:
        - Layer: ``139``
        - ID: ``0xbe7e8ef1``

    Parameters:
        nonce: ``int`` ``128-bit``

    Returns:
        :obj:`ResPQ <pyrogram.raw.base.ResPQ>`
    """

    __slots__: List[str] = ["nonce"]

    ID = 0xbe7e8ef1
    QUALNAME = "functions.ReqPqMulti"

    def __init__(self, *, nonce: int) -> None:
        self.nonce = nonce  # int128

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ReqPqMulti":
        # No flags
        
        nonce = Int128.read(b)
        
        return ReqPqMulti(nonce=nonce)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int128(self.nonce))
        
        return b.getvalue()