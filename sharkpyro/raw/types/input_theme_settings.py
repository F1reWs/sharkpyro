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


class InputThemeSettings(TLObject):  # type: ignore
    """This object is a constructor of the base type :obj:`~pyrogram.raw.base.InputThemeSettings`.

    Details:
        - Layer: ``139``
        - ID: ``0x8fde504f``

    Parameters:
        base_theme: :obj:`BaseTheme <pyrogram.raw.base.BaseTheme>`
        accent_color: ``int`` ``32-bit``
        message_colors_animated (optional): ``bool``
        outbox_accent_color (optional): ``int`` ``32-bit``
        message_colors (optional): List of ``int`` ``32-bit``
        wallpaper (optional): :obj:`InputWallPaper <pyrogram.raw.base.InputWallPaper>`
        wallpaper_settings (optional): :obj:`WallPaperSettings <pyrogram.raw.base.WallPaperSettings>`
    """

    __slots__: List[str] = ["base_theme", "accent_color", "message_colors_animated", "outbox_accent_color", "message_colors", "wallpaper", "wallpaper_settings"]

    ID = 0x8fde504f
    QUALNAME = "types.InputThemeSettings"

    def __init__(self, *, base_theme: "raw.base.BaseTheme", accent_color: int, message_colors_animated: Union[None, bool] = None, outbox_accent_color: Union[None, int] = None, message_colors: Union[None, List[int]] = None, wallpaper: "raw.base.InputWallPaper" = None, wallpaper_settings: "raw.base.WallPaperSettings" = None) -> None:
        self.base_theme = base_theme  # BaseTheme
        self.accent_color = accent_color  # int
        self.message_colors_animated = message_colors_animated  # flags.2?true
        self.outbox_accent_color = outbox_accent_color  # flags.3?int
        self.message_colors = message_colors  # flags.0?Vector<int>
        self.wallpaper = wallpaper  # flags.1?InputWallPaper
        self.wallpaper_settings = wallpaper_settings  # flags.1?WallPaperSettings

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputThemeSettings":
        flags = Int.read(b)
        
        message_colors_animated = True if flags & (1 << 2) else False
        base_theme = TLObject.read(b)
        
        accent_color = Int.read(b)
        
        outbox_accent_color = Int.read(b) if flags & (1 << 3) else None
        message_colors = TLObject.read(b, Int) if flags & (1 << 0) else []
        
        wallpaper = TLObject.read(b) if flags & (1 << 1) else None
        
        wallpaper_settings = TLObject.read(b) if flags & (1 << 1) else None
        
        return InputThemeSettings(base_theme=base_theme, accent_color=accent_color, message_colors_animated=message_colors_animated, outbox_accent_color=outbox_accent_color, message_colors=message_colors, wallpaper=wallpaper, wallpaper_settings=wallpaper_settings)

    def write(self) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.message_colors_animated else 0
        flags |= (1 << 3) if self.outbox_accent_color is not None else 0
        flags |= (1 << 0) if self.message_colors else 0
        flags |= (1 << 1) if self.wallpaper is not None else 0
        flags |= (1 << 1) if self.wallpaper_settings is not None else 0
        b.write(Int(flags))
        
        b.write(self.base_theme.write())
        
        b.write(Int(self.accent_color))
        
        if self.outbox_accent_color is not None:
            b.write(Int(self.outbox_accent_color))
        
        if self.message_colors:
            b.write(Vector(self.message_colors, Int))
        
        if self.wallpaper is not None:
            b.write(self.wallpaper.write())
        
        if self.wallpaper_settings is not None:
            b.write(self.wallpaper_settings.write())
        
        return b.getvalue()
