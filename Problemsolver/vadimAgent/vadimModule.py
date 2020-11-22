from common import ScModule, ScKeynodes, ScPythonEventType
from keynodes import Keynodes
from vadimAgent import vadimAgent

from sc import *


class vadimModule(ScModule):

    def __init__(self):
        ScModule.__init__(
            self,
            ctx=__ctx__,
            cpp_bridge=__cpp_bridge__,
            keynodes=[
            ],
            )

    def OnInitialize(self, params):
        print('Initialize Hello module')        
        kHello = self.ctx.HelperResolveSystemIdtf("vadimhello", ScType.NodeConst)
        kWorld = self.ctx.HelperResolveSystemIdtf("world", ScType.NodeConst)
        
        agent = vadimAgent(self)
        agent.Register(kHello, ScPythonEventType.AddOutputEdge)        

       

    def OnShutdown(self):        
        print('Shutting down Hello module')  


service = vadimModule()
service.Run()
