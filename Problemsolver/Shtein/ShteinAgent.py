from common import ScModule, ScAgent, ScEventParams
from sc import *


class ShteinAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("shtein agent init")
 
        class_find = evt.other_addr
        ans= self.module.ctx.HelperResolveSystemIdtf("answerForAgent4", ScType.NodeConstClass)

        print("0")
        body = self.module.ctx.HelperResolveSystemIdtf("nrel_for_body", ScType.NodeConstNoRole)
        print("1")
        mod= self.module.ctx.HelperResolveSystemIdtf("nrel_access_modifier", ScType.NodeConstNoRole)
        method = self.module.ctx.HelperResolveSystemIdtf("nrel_method", ScType.NodeConstNoRole)
        print("2")

        for_cycle= self.module.ctx.HelperResolveSystemIdtf("concept_for", ScType.NodeConstClass)
        print("3")

       
        method_find= self.module.ctx.Iterator5(class_find, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, method)
        body_find =  self.module.ctx.Iterator3(method_find.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConst )
        

        acc_find=  self.module.ctx.Iterator5(class_find, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, mod)
        
        self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, ans,acc_find.Get(2))


        

        print(method_find.Get(2))

        
        print("4")
        while  body_find.Next():
            iterate_cycles= self.module.ctx.Iterator3(for_cycle,ScType.EdgeAccessConstPosPerm,  body_find.Get(2) )
            print("while")
            
            if iterate_cycles.IsValid():
                self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, check_for, iterate_cycles.Get(2))
                print("if1")

            iterate_cycles =  self.module.ctx.Iterator3(for_cycle, ScType.EdgeAccessConstPosPerm,  body_find.Get(2))

            iterate_body = self.module.ctx.Iterator5(for_cycle,ScType.EdgeAccessConstPosPerm, ScType.NodeConst,ScType.EdgeAccessConstPosPer ,nrel_iteration_body )

            if iterate_body.IsValid():
                iterate_body_check = self.module.ctx.Iterator3 (iterate_body.Get(4), ScType.EdgeAccessConstPosPerm, ScType.NodeConst)
                print("if2")


                if not iterate_body_check.Next():
                    print("if3")
                
                   
                    return ScResult.Ok  


