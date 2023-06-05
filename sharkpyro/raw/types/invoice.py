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


class Invoice(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.Invoice`.

    Details:
        - Layer: ``139``
        - ID: ``0xcd886e0``

    Parameters:
        currency: ``str``
        prices: List of :obj:`LabeledPrice <pyrogram.raw.base.LabeledPrice>`
        test (optional): ``bool``
        name_requested (optional): ``bool``
        phone_requested (optional): ``bool``
        email_requested (optional): ``bool``
        shipping_address_requested (optional): ``bool``
        flexible (optional): ``bool``
        phone_to_provider (optional): ``bool``
        email_to_provider (optional): ``bool``
        max_tip_amount (optional): ``int`` ``64-bit``
        suggested_tip_amounts (optional): List of ``int`` ``64-bit``
    """

    __slots__: List[str] = ["currency", "prices", "test", "name_requested", "phone_requested", "email_requested", "shipping_address_requested", "flexible", "phone_to_provider", "email_to_provider", "max_tip_amount", "suggested_tip_amounts"]

    ID = 0xcd886e0
    QUALNAME = "types.Invoice"

    def __init__(self, *, currency: str, prices: List["raw.base.LabeledPrice"], test: Union[None, bool] = None, name_requested: Union[None, bool] = None, phone_requested: Union[None, bool] = None, email_requested: Union[None, bool] = None, shipping_address_requested: Union[None, bool] = None, flexible: Union[None, bool] = None, phone_to_provider: Union[None, bool] = None, email_to_provider: Union[None, bool] = None, max_tip_amount: Union[None, int] = None, suggested_tip_amounts: Union[None, List[int]] = None) -> None:
        self.currency = currency  # string
        self.prices = prices  # Vector<LabeledPrice>
        self.test = test  # flags.0?true
        self.name_requested = name_requested  # flags.1?true
        self.phone_requested = phone_requested  # flags.2?true
        self.email_requested = email_requested  # flags.3?true
        self.shipping_address_requested = shipping_address_requested  # flags.4?true
        self.flexible = flexible  # flags.5?true
        self.phone_to_provider = phone_to_provider  # flags.6?true
        self.email_to_provider = email_to_provider  # flags.7?true
        self.max_tip_amount = max_tip_amount  # flags.8?long
        self.suggested_tip_amounts = suggested_tip_amounts  # flags.8?Vector<long>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Invoice":
        flags = Int.read(b)
        
        test = True if flags & (1 << 0) else False
        name_requested = True if flags & (1 << 1) else False
        phone_requested = True if flags & (1 << 2) else False
        email_requested = True if flags & (1 << 3) else False
        shipping_address_requested = True if flags & (1 << 4) else False
        flexible = True if flags & (1 << 5) else False
        phone_to_provider = True if flags & (1 << 6) else False
        email_to_provider = True if flags & (1 << 7) else False
        currency = String.read(b)
        
        prices = TLObject.read(b)
        
        max_tip_amount = Long.read(b) if flags & (1 << 8) else None
        suggested_tip_amounts = TLObject.read(b, Long) if flags & (1 << 8) else []
        
        return Invoice(currency=currency, prices=prices, test=test, name_requested=name_requested, phone_requested=phone_requested, email_requested=email_requested, shipping_address_requested=shipping_address_requested, flexible=flexible, phone_to_provider=phone_to_provider, email_to_provider=email_to_provider, max_tip_amount=max_tip_amount, suggested_tip_amounts=suggested_tip_amounts)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.test else 0
        flags |= (1 << 1) if self.name_requested else 0
        flags |= (1 << 2) if self.phone_requested else 0
        flags |= (1 << 3) if self.email_requested else 0
        flags |= (1 << 4) if self.shipping_address_requested else 0
        flags |= (1 << 5) if self.flexible else 0
        flags |= (1 << 6) if self.phone_to_provider else 0
        flags |= (1 << 7) if self.email_to_provider else 0
        flags |= (1 << 8) if self.max_tip_amount is not None else 0
        flags |= (1 << 8) if self.suggested_tip_amounts else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Vector(self.prices))
        
        if self.max_tip_amount is not None:
            b.write(Long(self.max_tip_amount))
        
        if self.suggested_tip_amounts:
            b.write(Vector(self.suggested_tip_amounts, Long))
        
        return b.getvalue()
