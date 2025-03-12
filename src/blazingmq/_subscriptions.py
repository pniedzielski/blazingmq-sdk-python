# Copyright 2024 Bloomberg Finance L.P.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import annotations

from typing import Optional


class Subscription:
    """A value semantic type representing the settings for a subscription.

    Each option can be set either by passing it as a keyword argument when
    constructing a *Subscription* instance, or by setting it as an attribute on
    a constructed instance.

    The default for every option is `None`.
    """

    VERSION_1 = 1
    """The simple evaluator subscription expression version."""

    def __init__(
        self,
        expression: str,
        version: int = VERSION_1,
        max_unconfirmed_messages: Optional[int] = None,
        max_unconfirmed_bytes: Optional[int] = None,
        consumer_priority: Optional[int] = None,
    ) -> None:
        self.expression = expression
        self.version = version
        self.max_unconfirmed_messages = max_unconfirmed_messages
        self.max_unconfirmed_bytes = max_unconfirmed_bytes
        self.consumer_priority = consumer_priority

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Subscription):
            return False
        return (
            self.expression == other.expression
            and self.version == other.version
            and self.max_unconfirmed_messages == other.max_unconfirmed_messages
            and self.max_unconfirmed_bytes == other.max_unconfirmed_bytes
            and self.consumer_priority == other.consumer_priority
        )

    def __ne__(self, other: object) -> bool:
        return not self == other

    def __repr__(self) -> str:
        attrs = (
            "expression",
            "version",
            "max_unconfirmed_messages",
            "max_unconfirmed_bytes",
            "consumer_priority",
        )

        params = []
        for attr in attrs:
            value = getattr(self, attr)
            if value is not None:
                params.append(f"{attr}={value!r}")

        return f"Subscription({', '.join(params)})"
