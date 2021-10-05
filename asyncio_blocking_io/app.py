# -*- coding: utf-8 -*-
"""ASGI server."""
import argparse
import asyncio
import datetime
import sys
import time

import uvicorn
from fastapi import FastAPI

from asyncio_blocking_io import __version__

app = FastAPI(
    title="Asyncio and Blocking Code",
    description="A didatic API that that shows issues when dealing with (IO) blocking code in async Python.",
    version=__version__,
)

SLEEP_TIME_IN_SECONDS = 2


@app.get("/async_def_and_blocking_io")
async def async_def_and_blocking_io():
    """
    Handles GET requests to /async_def_and_blocking_io.

    Returns
    -------
    text
    """
    time.sleep(SLEEP_TIME_IN_SECONDS)
    return datetime.datetime.now().strftime("%H:%M:%S")


@app.get("/def_and_blocking_io")
def def_and_blocking_io():
    """
    Handles GET requests to /def_and_blocking_io.

    Returns
    -------
    text
    """
    time.sleep(SLEEP_TIME_IN_SECONDS)
    return datetime.datetime.now().strftime("%H:%M:%S")


@app.get("/async_def_non_blocking_io")
async def async_def_non_blocking_io():
    """
    Handles GET requests to /async_def_non_blocking_io.

    Returns
    -------
    text
    """
    await asyncio.sleep(SLEEP_TIME_IN_SECONDS)
    return datetime.datetime.now().strftime("%H:%M:%S")


@app.get("/async_def_blocking_io_run_in_executor")
async def async_def_blocking_io_run_in_executor():
    """
    Handles GET requests to /async_def_non_blocking_io.

    Returns
    -------
    text
    """
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, time.sleep, SLEEP_TIME_IN_SECONDS)
    return datetime.datetime.now().strftime("%H:%M:%S")


def parse_args(args):
    """Takes argv and parses API options."""
    parser = argparse.ArgumentParser(
        description="Asyncio and Blocking Code",
    )
    parser.add_argument(
        "--host", type=str, default="127.0.0.1", help="Host for HTTP server (default: 127.0.0.1)",
    )
    parser.add_argument(
        "--port", type=int, default=8000, help="Port for HTTP server (default: 8000)",
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    args = parse_args(sys.argv[1:])

    uvicorn.run(app, host=args.host, port=args.port)
