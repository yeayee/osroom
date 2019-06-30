#!/usr/bin/env python
# -*-coding:utf-8-*-
from tld import get_tld

__author__ = "Allen Woo"


def get_domain(url):
    """
    获取url中的全域名
    :param url:
    :return:
    """
    try:
        res = get_tld(url, as_object=True)
    except:
        return False
    return "{}.{}".format(res.subdomain, res.tld)
