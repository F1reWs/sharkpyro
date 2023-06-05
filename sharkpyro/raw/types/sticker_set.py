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


class StickerSet(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.StickerSet`.

    Details:
        - Layer: ``139``
        - ID: ``0xd7df217a``

    Parameters:
        id: ``int`` ``64-bit``
        access_hash: ``int`` ``64-bit``
        title: ``str``
        short_name: ``str``
        count: ``int`` ``32-bit``
        hash: ``int`` ``32-bit``
        archived (optional): ``bool``
        official (optional): ``bool``
        masks (optional): ``bool``
        animated (optional): ``bool``
        videos (optional): ``bool``
        installed_date (optional): ``int`` ``32-bit``
        thumbs (optional): List of :obj:`PhotoSize <pyrogram.raw.base.PhotoSize>`
        thumb_dc_id (optional): ``int`` ``32-bit``
        thumb_version (optional): ``int`` ``32-bit``
    """

    __slots__: List[str] = ["id", "access_hash", "title", "short_name", "count", "hash", "archived", "official", "masks", "animated", "videos", "installed_date", "thumbs", "thumb_dc_id", "thumb_version"]

    ID = 0xd7df217a
    QUALNAME = "types.StickerSet"

    def __init__(self, *, id: int, access_hash: int, title: str, short_name: str, count: int, hash: int, archived: Union[None, bool] = None, official: Union[None, bool] = None, masks: Union[None, bool] = None, animated: Union[None, bool] = None, videos: Union[None, bool] = None, installed_date: Union[None, int] = None, thumbs: Union[None, List["raw.base.PhotoSize"]] = None, thumb_dc_id: Union[None, int] = None, thumb_version: Union[None, int] = None) -> None:
        self.id = id  # long
        self.access_hash = access_hash  # long
        self.title = title  # string
        self.short_name = short_name  # string
        self.count = count  # int
        self.hash = hash  # int
        self.archived = archived  # flags.1?true
        self.official = official  # flags.2?true
        self.masks = masks  # flags.3?true
        self.animated = animated  # flags.5?true
        self.videos = videos  # flags.6?true
        self.installed_date = installed_date  # flags.0?int
        self.thumbs = thumbs  # flags.4?Vector<PhotoSize>
        self.thumb_dc_id = thumb_dc_id  # flags.4?int
        self.thumb_version = thumb_version  # flags.4?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerSet":
        flags = Int.read(b)
        
        archived = True if flags & (1 << 1) else False
        official = True if flags & (1 << 2) else False
        masks = True if flags & (1 << 3) else False
        animated = True if flags & (1 << 5) else False
        videos = True if flags & (1 << 6) else False
        installed_date = Int.read(b) if flags & (1 << 0) else None
        id = Long.read(b)
        
        access_hash = Long.read(b)
        
        title = String.read(b)
        
        short_name = String.read(b)
        
        thumbs = TLObject.read(b) if flags & (1 << 4) else []
        
        thumb_dc_id = Int.read(b) if flags & (1 << 4) else None
        thumb_version = Int.read(b) if flags & (1 << 4) else None
        count = Int.read(b)
        
        hash = Int.read(b)
        
        return StickerSet(id=id, access_hash=access_hash, title=title, short_name=short_name, count=count, hash=hash, archived=archived, official=official, masks=masks, animated=animated, videos=videos, installed_date=installed_date, thumbs=thumbs, thumb_dc_id=thumb_dc_id, thumb_version=thumb_version)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.archived else 0
        flags |= (1 << 2) if self.official else 0
        flags |= (1 << 3) if self.masks else 0
        flags |= (1 << 5) if self.animated else 0
        flags |= (1 << 6) if self.videos else 0
        flags |= (1 << 0) if self.installed_date is not None else 0
        flags |= (1 << 4) if self.thumbs else 0
        flags |= (1 << 4) if self.thumb_dc_id is not None else 0
        flags |= (1 << 4) if self.thumb_version is not None else 0
        b.write(Int(flags))
        
        if self.installed_date is not None:
            b.write(Int(self.installed_date))
        
        b.write(Long(self.id))
        
        b.write(Long(self.access_hash))
        
        b.write(String(self.title))
        
        b.write(String(self.short_name))
        
        if self.thumbs:
            b.write(Vector(self.thumbs))
        
        if self.thumb_dc_id is not None:
            b.write(Int(self.thumb_dc_id))
        
        if self.thumb_version is not None:
            b.write(Int(self.thumb_version))
        
        b.write(Int(self.count))
        
        b.write(Int(self.hash))
        
        return b.getvalue()
