#!/usr/bin/env python
"""
Provides all asset functions
"""
import json
import requests


def get_asset_list(self):
    """
    Get the list of all native assets (paginated)

    :return: list with all asset list.
    :rtype: list.
    """
    asset_list = requests.get(self.ASSET_LIST_URL, timeout=10)
    asset_list = json.loads(asset_list.content)
    return asset_list


def get_asset_address_list(self, asset_policy, asset_name):
    """
    Get the list of all addresses holding a given asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all addresses.
    :rtype: list.
    """
    info = requests.get(f"{self.ASSET_ADDRESS_LIST_URL}{asset_policy}&_asset_name={asset_name}", timeout=10)
    # info =requests.get("{}{}&_asset_name={}".format(self.ASSET_ADDRESS_LIST_URL, asset_policy, asset_name), timeout=10)
    # info = requests.get(self.ASSET_ADDRESS_LIST_URL + asset_policy + "&_asset_name=" + asset_name, timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_info(self, asset_policy, asset_name):
    """
    Get the information of an asset including first minting & token registry metadata.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of all asset info.
    :rtype: list.
    """
    info = requests.get(f"{self.ASSET_INFO_URL}{asset_policy}&_asset_name={asset_name}", timeout=10)
    # info = requests.get("{}{}&_asset_name={}".format(self.ASSET_INFO_URL, asset_policy, asset_name), timeout=10)
    # info = requests.get(self.ASSET_INFO_URL + str(asset_policy) + "&_asset_name=" + str(asset_name), timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_history(self, asset_policy, asset_name):
    """
    Get the mint/burn history of an asset.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset mint/burn history.
    :rtype: list.
    """
    history = requests.get(f"{self.ASSET_HISTORY_URL}{asset_policy}&_asset_name={asset_name}", timeout=10)
    # history = requests.get("{}{}&_asset_name={}".format(self.ASSET_HISTORY_URL, asset_policy, asset_name), timeout=10)
    # history = requests.get(self.ASSET_HISTORY_URL + str(asset_policy) + "&_asset_name=" + str(asset_name), timeout=10)
    history = json.loads(history.content)
    return history


def get_asset_policy_info(self, asset_policy):
    """
    Get the information for all assets under the same policy.

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :return: list of all mint/burn transactions for an asset
    :rtype: list.
    """
    info = requests.get(f"{self.ASSET_POLICY_INFO_URL}{asset_policy}", timeout=10)
    # info = requests.get("{}{}".format(self.ASSET_POLICY_INFO_URL, asset_policy), timeout=10)
    # info = requests.get(self.ASSET_POLICY_INFO_URL + asset_policy, timeout=10)
    info = json.loads(info.content)
    return info


def get_asset_summary(self, asset_policy, asset_name):
    """
    Get the summary of an asset (total transactions exclude minting/total wallets include only
    wallets with asset balance).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :return: list of asset summary information.
    :rtype: list.
    """
    summary = requests.get(f"{self.ASSET_SUMMARY_URL}{asset_policy}&_asset_name={asset_name}", timeout=10)
    # summary = requests.get("{}{}&_asset_name={}".format(self.ASSET_SUMMARY_URL, asset_policy, asset_name), timeout=10)
    # summary = requests.get(self.ASSET_SUMMARY_URL + asset_policy + "&_asset_name=" + asset_name, timeout=10)
    summary = json.loads(summary.content)
    return summary


def get_asset_txs(self, asset_policy, asset_name, after_block_height=0):
    """
    Get the list of all asset transaction hashes (newest first).

    :param str asset_policy: asset Policy ID in hexadecimal format (hex).
    :param str asset_name: string with Asset Name in hexadecimal format (hex).
    :param int after_block_height: Block height for specifying time delta, if not data start from 0
    :return: list of all asset hashes transactions.
    :rtype: list.
    """
    txs = requests.get(f"{self.ASSET_TXS_URL}{asset_policy}&_asset_name={asset_name}&_after_block_height={after_block_height}", timeout=10)
    #txs = requests.get("{}{}&_asset_name={}&_after_block_height={}".format(self.ASSET_TXS_URL, asset_policy, asset_name, after_block_height), timeout=10)
    #txs = requests.get(self.ASSET_TXS_URL + asset_policy + "&_asset_name=" + asset_name + \
    #     "&_after_block_height=" + str(after_block_height), timeout=10)
    txs = json.loads(txs.content)
    return txs
    