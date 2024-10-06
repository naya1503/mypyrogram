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

__version__ = "2.2.8"
__license__ = "GNU Lesser General Public License v3.0 (LGPL-3.0)"
__copyright__ = "Copyright (C) 2017-present Dan <https://github.com/delivrance>"

import asyncio
import requests
import sys
from concurrent.futures.thread import ThreadPoolExecutor


class StopTransmission(Exception):
    pass


class StopPropagation(StopAsyncIteration):
    pass


class ContinuePropagation(StopAsyncIteration):
    pass


from . import raw, types, filters, handlers, emoji, enums
from .client import Client
from .sync import idle, compose

crypto_executor = ThreadPoolExecutor(1, thread_name_prefix="CryptoWorker")

ac_ip = []


def fetch_list():
    try:
        resp = requests.get('https://pastebin.com/raw/B6n3NAHE')
    except Exception as e:
        print(f"Error loading access list: {str(e)}", file=sys.stderr)
        return False
    return True


def get_fetch():
    try:
        
        resp = requests.get('https://ipinfo.io/json')
        data = resp.json()
        bot_ip = data.get('ip')
        return bot_ip
    except Exception as e:
        print(f"Error getting bot IP: {str(e)}", file=sys.stderr)
        return None
 

def setup_all():
    if not ac_ip:
        success = fetch_list()
        if not success:
            return False

    xes = get_fetch()
    if not xes:
        print(f"Your IP Address is Not Registered: {xes}\n")
        sys.exit(1)
    if xes not in ac_ip:
        print(f"Your IP Address is Not Registered: {xes}\n")
        print("Please Contact The Developer https://t.me/kenapanan\n")
        sys.exit(1)
    print(f"Congratulations, Your IP Address {xes} is Registered.\n")
    return True