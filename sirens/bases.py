#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
@date: 2013-06-16
@author: shell.xu
'''

def set_cmdcfg(cfg, d):
    keys = set(cfg.keys()) & set(d.keys())
    return [d[key](cfg[key]) for key in keys]

def set_appcfg(app, cfg, d):
    keys = set(cfg.keys()) & set(d.keys())
    return [d[key](app, cfg[key], cfg) for key in keys]

class RegNameClsBase(object):
    @classmethod
    def register(cls, name, funcname=None):
        l = getattr(cls, name)
        def inner(func):
            fn = funcname or func.__name__
            l[fn] = func
            cls.keyset.add(fn)
            return func
        return inner

class RegClsBase(object):
    @classmethod
    def register(cls, funcname=None):
        def inner(func):
            fn = funcname or func.__name__
            cls.regs[fn] = func
            cls.keyset.add(fn)
            return func
        return inner

