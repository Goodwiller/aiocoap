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

logging.basicConfig(level=logging.INFO)

async def main():
    protocol = await Context.create_client_context()

    request = Message(code=GET, uri='coap://vs0.inf.ethz.ch/obs', observe=0)

    pr = protocol.request(request)

    r = await pr.response
    print("First response: %s\n%r"%(r, r.payload))

    async for r in pr.observation:
        print("Next result: %s\n%r"%(r, r.payload))

        pr.observation.cancel()
        break
    print("Loop ended, sticking around")
    await asyncio.sleep(50)

if __name__ == "__main__":
    asyncio.run(main())
