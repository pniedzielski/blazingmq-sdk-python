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

import pytest

import blazingmq


def test_subscription_repr():
    # WHEN
    one = blazingmq.Subscription(
        expression="foo == 1",
        version=blazingmq.Subscription.VERSION_1,
        consumer_priority=100,
        max_unconfirmed_bytes=1,
        max_unconfirmed_messages=10
    )
    # THEN
    assert (
        "Subscription("
        "expression=\"foo == 1\","
        " version=1,"
        " max_unconfirmed_messages=10,"
        " max_unconfirmed_bytes=1,"
        " consumer_priority=100)" == repr(one)
    )


def test_subscription_default_repr():
    # WHEN
    subscription = blazingmq.Subscription("foo == 1")  # not defaultable
    # THEN
    assert "Subscription(expression=\"foo == 1\")" == repr(subscription)


def test_subscription_default_to_none():
    # WHEN
    subscription = blazingmq.Subscription("foo == 1")
    # THEN
    assert subscription.expression == "foo == 1"  # not defaultable
    assert subscription.version is None
    assert subscription.consumer_priority is None
    assert subscription.max_unconfirmed_bytes is None
    assert subscription.max_unconfirmed_messages is None


def test_subscription_equality():
    # GIVEN
    left = blazingmq.Subscription()

    # WHEN
    right = blazingmq.Subscription()

    # THEN
    assert left == right
    assert (left != right) is False


@pytest.mark.parametrize(
    "right",
    [
        None,
        "string",
        blazingmq.Subscription("bar != 2"),
        blazingmq.Subscription("foo == 1", version=0),
        blazingmq.Subscription("foo == 1", max_unconfirmed_messages=1),
        blazingmq.Subscription("foo == 1", max_unconfirmed_bytes=1),
        blazingmq.Subscription("foo == 1", consumer_priority=1),
    ],
)
def test_subscription_other_inequality(right):
    # GIVEN
    left = blazingmq.Subscription("foo == 1")

    # THEN
    assert not left == right
