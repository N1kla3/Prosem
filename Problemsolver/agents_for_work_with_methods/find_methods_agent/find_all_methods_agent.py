from common import ScModule, ScAgent, ScEventParams
from sc import *

class Find_all_methods_agent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("myAgent : RunImpl")
        codeblock = evt.other_addr
        all_methods = self.module.ctx.HelperResolveSystemIdtf("concept_methods", ScType.NodeConstClass)
        
        n_method = self.module.ctx.HelperResolveSystemIdtf("nrel_method", ScType.NodeConstNoRole)
        find_all_methods = self.module.ctx.Iterator5(codeblock, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, n_method) 
        while find_all_methods.Next():
            self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, all_methods, find_all_methods.Get(2))
        return ScResult.Ok

            
