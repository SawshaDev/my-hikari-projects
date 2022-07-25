
from __future__ import annotations
import abc
import calendar
import datetime
import logging
from logging.handlers import RotatingFileHandler
import time
import timeago as timesince
import typing as t
import aiohttp

import hikari
import lightbulb
from bot import SawshaBot


class Plugin(lightbulb.Plugin):
    @property
    def bot(self) -> SawshaBot:
        return t.cast(SawshaBot, self.app)



class Context(lightbulb.Context):
    def __init__(self):
        setattr(self, 'session', aiohttp.ClientSession())

    @property
    def bot(self) -> SawshaBot:
        return t.cast(SawshaBot, self.app)

    @property
    def app(self) -> SawshaBot:
        return t.cast(SawshaBot, self.app)


class SlashContext(Context, lightbulb.SlashContext):
    ...

class PrefixContext(Context, lightbulb.PrefixContext):
    ...

def date(target, clock: bool = True, seconds: bool = False, ago: bool = False, only_ago: bool = False, raw: bool = False):
    if isinstance(target, int) or isinstance(target, float):
        target = datetime.datetime.utcfromtimestamp(target)

    if target is None:
        return 'N/A'

    if raw:
        if clock:
            timestamp = target.strftime("%d %B %Y, %H:%M")
        elif seconds:
            timestamp = target.strftime("%d %B %Y, %H:%M:%S")
        else:
            timestamp = target.strftime("%d %B %Y")

        if isinstance(target, int) or isinstance(target, float):
            target = datetime.datetime.utcfromtimestamp(target)
            target = calendar.timegm(target.timetuple())

        if ago:
            timestamp += f" ({timesince.format(target)})"
        if only_ago:
            timestamp = timesince.format(target)

        return f"{timestamp} (UTC)"
    else:
        unix = int(time.mktime(target.timetuple()))
        timestamp = f"<t:{unix}:{'f' if clock else 'D'}>"
        if ago:
            timestamp += f" (<t:{unix}:R>)"
        if only_ago:
            timestamp = f"<t:{unix}:R>"
        return timestamp