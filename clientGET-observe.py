#!/usr/bin/env python3

# SPDX-FileCopyrightText: Christian Amsüss and the aiocoap contributors
#
# SPDX-License-Identifier: MIT

"""This is a usage example of aiocoap that demonstrates how to implement a
simple client. See the "Usage Examples" section in the aiocoap documentation
for some more information."""

import logging
import asyncio

from aiocoap import *

logging.basicConfig(level=logging.DEBUG)


async def main():
    protocol = await Context.create_client_context()

    request_msg = Message(code=GET, uri='coap://localhost/time', observe = 0)

    request_obj = protocol.request(request_msg)

    counter = 0
    async for r in request_obj.observation:
        print(r.payload)
        print("_________________________________")
        counter = counter + 1
        if (counter == 3):
            break

    await asyncio.sleep(10)

    request_obj_new = await protocol.re_register(request_obj)

    counter = 0
    async for r in request_obj_new.observation:
        print(r.payload)
        print("_________________________________")
        counter = counter + 1
        if (counter == 3):
            break

    await protocol.cancel_observation(request_obj_new, urgent = True)

    await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())
