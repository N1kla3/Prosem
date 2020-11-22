from NoDiscardAgent import NoDiscardAgent
from common import ScModule, ScPythonEventType
from sc import *


class NoDiscardModule(ScModule):

    def __init__(self):
        ScModule.__init__(
                self,
                ctx=__ctx__,
                cpp_bridge=__cpp_bridge__,
                keynodes=[
                    ],
                )

    def OnInitialize(self, params):
        print('Initialize NoDiscard module')
        start = self.ctx.HelperResolveSystemIdtf("Discard_question", ScType.NodeConstClass)

        agent_find_functions = NoDiscardAgent(self)
        agent_find_functions.Register(start, ScPythonEventType.AddOutputEdge)        


    def OnShutdown(self):
        print('Shutdown NoDicard Module')


service = NoDiscardModule()
service.Run()
