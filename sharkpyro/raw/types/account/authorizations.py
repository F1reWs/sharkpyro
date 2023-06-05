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


class Authorizations(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.account.Authorizations`.

    Details:
        - Layer: ``139``
        - ID: ``0x4bff8ea0``

    Parameters:
        authorization_ttl_days: ``int`` ``32-bit``
        authorizations: List of :obj:`Authorization <pyrogram.raw.base.Authorization>`

    See Also:
        This object can be returned by 1 method:

        .. hlist::
            :columns: 2

            - :obj:`account.GetAuthorizations <pyrogram.raw.functions.account.GetAuthorizations>`
    """

    __slots__: List[str] = ["authorization_ttl_days", "authorizations"]

    ID = 0x4bff8ea0
    QUALNAME = "types.account.Authorizations"

    def __init__(self, *, authorization_ttl_days: int, authorizations: List["raw.base.Authorization"]) -> None:
        self.authorization_ttl_days = authorization_ttl_days  # int
        self.authorizations = authorizations  # Vector<Authorization>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Authorizations":
        # No flags
        
        authorization_ttl_days = Int.read(b)
        
        authorizations = TLObject.read(b)
        
        return Authorizations(authorization_ttl_days=authorization_ttl_days, authorizations=authorizations)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.authorization_ttl_days))
        
        b.write(Vector(self.authorizations))
        
        return b.getvalue()
