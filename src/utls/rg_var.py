#coding=utf-8
import sys,re,os,string,logging
import setting
import interface

import rg_var_impl
import tpl.tpl_var

rg_vars = rg_var_impl.rgvar_god()

def clean() :
    rg_vars.clean()

def keep():
    rg_vars.keep()

def rollback():
    rg_vars.rollback()

def import_context(context) :
    rg_vars.import_dict(context.__dict__)

def import_dict(d) :
    rg_vars.import_dict(d)

def value_of(exp):
    attr_vars = tpl.tpl_var.attr_proxy(rg_vars.current())
    tmp_exp   = rg_var_impl.env_exp.var_proc(str(exp),attr_vars)
    return rg_var_impl.env_exp.fun_proc(tmp_exp)


