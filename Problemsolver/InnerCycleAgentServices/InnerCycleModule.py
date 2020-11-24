from InnerCycleAgent import InnerCycleAgent
from common import ScModule, ScPythonEventType
from sc import *


class InnerCycleModule(ScModule):

    def __init__(self):
        ScModule.__init__(
                self,
                ctx=__ctx__,
                cpp_bridge=__cpp_bridge__,
                keynodes=[
                    ],
                )

    def OnInitialize(self, params):
        print('Initialize InnerCycle module')
        start = self.ctx.HelperResolveSystemIdtf("innercycle", ScType.NodeConstClass)

        agent = InnerCycleAgent(self)
        agent.Register(start, ScPythonEventType.AddOutputEdge)        


    def OnShutdown(self):
        print('Shutdown InnerCycle Module')
        start = self.ctx.HelperResolveSystemIdtf("innercycle", ScType.NodeConstClass)
        self.ctx.DeleteElement(start)


service = InnerCycleModule()
service.Run()
