# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Base functions for DM commands targeting the v2beta API."""

from googlecloudsdk.command_lib.deployment_manager import dm_base
from googlecloudsdk.core import apis


def GetClient():
  return apis.GetClientInstance('deploymentmanager', 'v2beta')


def GetMessages():
  return apis.GetMessagesModule('deploymentmanager', 'v2beta')


def GetResources():
  registry = dm_base.GetResources()
  registry.RegisterApiByName('deploymentmanager', 'v2beta')
  return registry
