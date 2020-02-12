# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

NODE_VERSION_DEFAULT = "10.14"
NETCORE_VERSION_DEFAULT = "2.2"
DOTNET_VERSION_DEFAULT = "4.7"
PYTHON_VERSION_DEFAULT = "3.7"
NETCORE_RUNTIME_NAME = "dotnetcore"
DOTNET_RUNTIME_NAME = "aspnet"
NODE_RUNTIME_NAME = "node"
PYTHON_RUNTIME_NAME = "python"
OS_DEFAULT = "Windows"
STATIC_RUNTIME_NAME = "static"  # not an official supported runtime but used for CLI logic
NODE_VERSIONS = ['4.4', '4.5', '6.2', '6.6', '6.9', '6.11', '8.0', '8.1', '8.9', '8.11', '10.1', '10.10', '10.14']
PYTHON_VERSIONS = ['3.7', '3.6', '2.7']
NETCORE_VERSIONS = ['1.0', '1.1', '2.1', '2.2']
DOTNET_VERSIONS = ['3.5', '4.7']
LINUX_SKU_DEFAULT = "P1V2"
FUNCTIONS_VERSIONS_FUNCTIONAPP = ['2', '3']
# functions version : default node version
NODE_VERSION_DEFAULT_FUNCTIONAPP = {
    '2': '~10',
    '3': '~12'
}
# functions version -> runtime : default runtime version
RUNTIME_TO_DEFAULT_VERSION_FUNCTIONAPP = {
    '2': {
        'node': '8',
        'dotnet': '2',
        'python': '3.7',
        'java': '8'
    },
    '3': {
        'node': '12',
        'dotnet': '3',
        'python': '3.7',
        'java': '8'
    }
}
# functions version -> runtime -> runtime version : container image
RUNTIME_TO_IMAGE_FUNCTIONAPP = {
    '2': {
        'node': {
            '8': 'mcr.microsoft.com/azure-functions/node:2.0-node8-appservice',
            '10': 'mcr.microsoft.com/azure-functions/node:2.0-node10-appservice'
        },
        'python': {
            '3.6': 'mcr.microsoft.com/azure-functions/python:2.0-python3.6-appservice',
            '3.7': 'mcr.microsoft.com/azure-functions/python:2.0-python3.7-appservice'
        },
        'dotnet': {
            '2': 'mcr.microsoft.com/azure-functions/dotnet:2.0-appservice'
        },
        'java': {
            '8': 'mcr.microsoft.com/azure-functions/java:2.0-java8-appservice'
        }
    },
    '3': {
        'node': {
            '10': 'mcr.microsoft.com/azure-functions/node:3.0-node10-appservice',
            '12': 'mcr.microsoft.com/azure-functions/node:3.0-node12-appservice'
        },
        'python': {
            '3.6': 'mcr.microsoft.com/azure-functions/python:3.0-python3.6-appservice',
            '3.7': 'mcr.microsoft.com/azure-functions/python:3.0-python3.7-appservice',
            '3.8': 'mcr.microsoft.com/azure-functions/python:3.0-python3.8-appservice'
        },
        'dotnet': {
            '3': 'mcr.microsoft.com/azure-functions/dotnet:3.0-appservice'
        },
        'java': {
            '8': 'mcr.microsoft.com/azure-functions/java:3.0-java8-appservice'
        }
    }
}
