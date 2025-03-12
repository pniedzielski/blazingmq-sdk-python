// Copyright 2024 Bloomberg Finance L.P.
// SPDX-License-Identifier: Apache-2.0
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

#ifndef INCLUDED_PYBMQ_SUBSCRIPTION
#define INCLUDED_PYBMQ_SUBSCRIPTION

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <bsl_optional.h>
#include <bsl_string.h>

namespace BloombergLP {
namespace pybmq {

/// A struct representing the configuration options for a consumer
/// subscription.  This type is used to ferry data from the Cython layer to the
/// pure C++ layer, where the BMQ subscription is constructed.
struct Subscription
{
  public:
    /// An integral handle for this subscription, allowing the user to
    /// correlate a message with the consumer subscription that allowed it to
    /// be consumed.
    int d_handle;

    /// An expression denoting messages that match this subscription.
    bsl::string d_expression;

    /// The version of the subscription handle language to instruct the broker
    /// to interpret `d_expression` with.  The value of this field *must* be
    /// one of the values supported by `bmqt::SubscriptionExpression::Enum`.
    int d_version;

    /// The maximum number of unconfirmed messages that may be sent to the
    /// consumer because of this subscription.
    bsl::optional<int> d_maxUnconfirmedMessages;

    /// The maximum size in bytes of unconfirmed messages that may be sent to
    /// the consumer because of this subscription.
    bsl::optional<int> d_maxUnconfirmedBytes;

    /// The priority of the consumer in round-robin delivery caused by this
    /// subscription.
    bsl::optional<int> d_consumerPriority;
};

}  // namespace pybmq
}  // namespace BloombergLP

#endif
