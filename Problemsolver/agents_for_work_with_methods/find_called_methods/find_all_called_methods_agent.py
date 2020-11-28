from common import ScModule, ScAgent, ScEventParams
from sc import *

class Find_all_called_methods_agent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("myAgent : RunImpl")
        codeblock = evt.other_addr
        all_called_methods = self.module.ctx.HelperResolveSystemIdtf("concept_called_methods", ScType.NodeConstClass)
        body = self.module.ctx.HelperResolveSystemIdtf("nrel_function_body", ScType.NodeConstNoRole)
        
        n_method = self.module.ctx.HelperResolveSystemIdtf("nrel_method", ScType.NodeConstNoRole)
        prototype_method = self.module.ctx.HelperResolveSystemIdtf("nrel_function_prototype", ScType.NodeConstNoRole)
        

        find_all_methods = self.module.ctx.Iterator5(codeblock, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, n_method) 
        while find_all_methods.Next():
            find_body = self.module.ctx.Iterator5(find_all_methods.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm,body)
            find_body.Next()
            iter_find_code_block = self.module.ctx.Iterator3( ScType.NodeConst, ScType.EdgeAccessConstPosPerm,find_body.Get(2))
            iter_find_code_block.Next()
            iter_find_rrel = self.module.ctx.Iterator5(iter_find_code_block.Get(0), ScType.EdgeAccessConstPosPerm, ScType.NodeConst, ScType.EdgeAccessConstPosPerm,ScType.NodeConstRole)
                    
            while iter_find_rrel.Next():
                if iter_find_code_block.IsValid():
                    if iter_find_rrel.IsValid():
                        find_called_function = self.module.ctx.Iterator5(iter_find_rrel.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm,prototype_method)
                        find_called_function.Next()
                        if find_called_function.IsValid():
                            self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, all_called_methods, find_called_function.Get(2))
        return ScResult.Ok

            
