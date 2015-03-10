#coding=utf-8
from res_base import *
from base     import *
_logger = logging.getLogger()

class rest(interface.resource):
    """
    生成 pylon rest 的索引
    !R.rest
        src: "$${PRJ_ROOT}/src/apps/api"
    """
    _src = None
    _dst = "${RUN_PATH}"
    def locate(self,context):
        self.src        = env_exp.value(self.src)
        self.dst        = env_exp.value(self.dst)
        self.out_idx    = os.path.join(self.dst , "_rest_conf.idx")

    def config(self,context):

        sed     = """sed -r "s/.+:class\s+(\S+)\s+.+\/\/\@REST_RULE:\s+(.+)/\\2 : \\1/g" """
        cmdtpl  = """grep --include "*.php" -i  -E "class .+ implements XService"  -R $SRC   |  """  + sed + " > $DST "
        cmd     = Template(cmdtpl).substitute(SRC =  self.src ,DST=self.out_idx)
        rg_sh.shexec.execmd(cmd,False)

    def check(self,context):
        self.check_print(os.path.exists(self.out_idx),self.out_idx)

    def clean_file(self,filename):
        cmdtpl = "if test -e $DST ; then rm -f  $DST ; fi ; "
        cmd    = Template(cmdtpl).substitute(DST=filename)
        rg_sh.shexec.execmd(cmd)

    def clean(self,context):
        self.clean_file(self.out_idx)
