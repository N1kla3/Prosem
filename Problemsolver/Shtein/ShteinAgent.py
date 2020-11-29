from common import ScModule, ScAgent, ScEventParams
from sc import *

class ShteinAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("myAgent : RunImpl")
        codeblock = evt.other_addr
        all_methods = self.module.ctx.HelperResolveSystemIdtf("concept_methods", ScType.NodeConstClass)
        bodyes= self.module.ctx.HelperResolveSystemIdtf("concept_cyclesWithoutBody", ScType.NodeConstClass) 
        body = self.module.ctx.HelperResolveSystemIdtf("nrel_iteration_body", ScType.NodeConstNoRole)
        foridt = self.module.ctx.HelperResolveSystemIdtf("concept_for", ScType.NodeConstClass)
        

        
        n_method = self.module.ctx.HelperResolveSystemIdtf("nrel_method", ScType.NodeConstNoRole)
        prototype_method = self.module.ctx.HelperResolveSystemIdtf("nrel_function_prototype", ScType.NodeConstNoRole)
        

        find_all_methods = self.module.ctx.Iterator5(codeblock, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, n_method) 

        while find_all_methods.Next():
            
            self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, all_methods, find_all_methods.Get(2))
            body_find= self.module.ctx.Iterator3(find_all_methods.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConst)

            while body_find.Next():
                
                cycle_find= self.module.ctx.Iterator3(body_find.Get(2), ScType.EdgeAccessConstPosPerm, foridt)
                if cycle_find.IsValid():
                   
                    cycle_body_find=  self.module.ctx.Iterator5(body_find.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm,body)
                    cycle_body_find.Next()
                    

                    body_check= self.module.ctx.Iterator3(cycle_body_find.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConst)
                   
                    count=0
                    while body_check.Next():
                        count+=1
                    print(count)

                    if count==0:
                        
                        self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, bodyes,body_find.Get(2))



            
            
        return ScResult.Ok
