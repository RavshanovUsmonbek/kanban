#!/usr/bin/python3
# coding=utf-8

#   Copyright 2022 getcarrier.io
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" RPC """
from datetime import datetime, timedelta
from sqlalchemy.dialects import postgresql  # pylint: disable=E0401
from typing import Dict, List
from sqlalchemy import update, or_, select, desc, func


from pylon.core.tools import log  # pylint: disable=E0611,E0401
from pylon.core.tools import web  # pylint: disable=E0611,E0401

from tools import db  # pylint: disable=E0401
from tools import db_tools  # pylint: disable=E0401
from tools import rpc_tools  # pylint: disable=E0401


class RPC:  # pylint: disable=E1101,R0903
    """ RPC Resource """

    # @web.rpc("issue_list_issues", "list_issues")
    # @rpc_tools.wrap_exceptions(RuntimeError)

