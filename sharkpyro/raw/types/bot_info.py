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


class BotInfo(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.BotInfo`.

    Details:
        - Layer: ``139``
        - ID: ``0x1b74b335``

    Parameters:
        user_id: ``int`` ``64-bit``
        description: ``str``
        commands: List of :obj:`BotCommand <pyrogram.raw.base.BotCommand>`
    """

    __slots__: List[str] = ["user_id", "description", "commands"]

    ID = 0x1b74b335
    QUALNAME = "types.BotInfo"

    def __init__(self, *, user_id: int, description: str, commands: List["raw.base.BotCommand"]) -> None:
        self.user_id = user_id  # long
        self.description = description  # string
        self.commands = commands  # Vector<BotCommand>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInfo":
        # No flags
        
        user_id = Long.read(b)
        
        description = String.read(b)
        
        commands = TLObject.read(b)
        
        return BotInfo(user_id=user_id, description=description, commands=commands)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(String(self.description))
        
        b.write(Vector(self.commands))
        
        return b.getvalue()
