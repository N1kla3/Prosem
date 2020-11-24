from common import ScModule, ScAgent, ScEventParams
from sc import *

class vadimAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("NoDiscardAgent : RunImpl")
        codeblock = evt.other_addr
        all_methods = self.module.ctx.HelperResolveSystemIdtf("concept_methods", ScType.NodeConstClass)
        n_method = self.module.ctx.HelperResolveSystemIdtf("nrel_method", ScType.NodeConstNoRole)
        method_modificator = self.module.ctx.HelperResolveSystemIdtf("nrel_main_idtf", ScType.NodeConstNoRole)
        all_called_methods = self.module.ctx.HelperResolveSystemIdtf("concept_called_methods", ScType.NodeConstClass)
        print('1')
        method = self.module.ctx.HelperResolveSystemIdtf("concept_called_method", ScType.NodeConstClass)
        print('2')
        
        iterate_find_name_method = self.module.ctx.Iterator5(codeblock, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, ScType.NodeConstNoRole)
        print('3')
        self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, all_methods, iterate_find_name_method.Get(2))
        try:
            while iterate_find_name_method.Next():
                print('while')
                iterate_mod_find_name_method = self.module.ctx.Iterator5(iterate_find_name_method.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, method_modificator)
        except:
            print('error')
        return ScResult.Ok

            
