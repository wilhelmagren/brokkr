"""
MIT License

Copyright (c) 2024 Wilhelm Ågren

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

File created: 2024-05-01
Last updated: 2024-05-01
"""

import logging

log = logging.getLogger(__name__)


def set_log_level(level: int) -> None:
    """ Set the threshold for the global logger to the specified `level`.
    Logging messages which are less severe than the `level` will be ignored,
    furthermore, logging messages which have severity `level` or higher will
    be emitted by whichever handler or handlers service this logger, unless
    a handler's level has been set to a higher severity level than `level`.

    Parameters
    ----------
    level : int
        The logger level to apply on the global logger and its handlers.

    """
    log.debug(f"Changing {log} level to `{level}`")
    log.setLevel(level)
    for handler in log.handlers:
        handler.setLevel(level)
    
