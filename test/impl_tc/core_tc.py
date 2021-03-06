#coding=utf-8
import interface
import base.tc_tools
import tc_data

from impl.rg_model import *
from impl.rg_prj import *


import  interface

class res_tc(base.tc_tools.rigger_tc):

    def test_context(self) :
        print("xxxx")
        context = interface.run_context()
        context.x = 1
        context.keep()
        context.x = 2
        self.assertEqual(context.x,2)
        context.rollback()
        self.assertEqual(context.x,1)


    def asst_call(self,res,context,method,inner_method):
        res.reset()
        run = res_runner(res)
        method(run,context)
        self.assertEqual(res.call_methods,['_before',inner_method,'_after'])

    def asst_res(self,res,method):
        name = res.name
        self.assertEqual(res.call_methods,[name + '_before',name + method,name + '_after'])

    def test_simple_res(self):
        res     = tc_data.simple_res()
        context = interface.run_context()
        self.asst_call(res, context,res_runner.config,'_config' )
        self.asst_call(res, context,res_runner.start,'_start' )
        self.asst_call(res, context,res_runner.stop,'_stop' )

    def test_box_res(self):
        reslist = []

        resbox = res_box()
        resbox.append( tc_data.simple_res("A") )
        resbox.append( tc_data.simple_res("B") )
        resbox.append( tc_data.simple_res("C") )

        context = interface.run_context()
        run     = res_runner(resbox)
        run.config(context)
        #æ£æ¥è°ç¨æ°æ®
        for res in resbox.res :
            self.asst_res(res,"_config")

