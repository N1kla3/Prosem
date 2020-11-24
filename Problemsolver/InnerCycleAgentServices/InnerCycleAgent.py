from common import ScModule, ScAgent, ScEventParams
from sc import *

class InnerCycleAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("InnerCycleAgent : RunImpl")
        class_find = evt.other_addr
        #check_functions = self.module.ctx.HelperResolveSystemIdtf("nodiscard_check_functions", ScType.NodeConstClass)
        #method = self.module.ctx.HelperResolveSystemIdtf("concept_called_method", ScType.NodeConstClass)
        #answer = self.module.ctx.HelperResolveSystemIdtf("NoDiscardAnswer", ScType.NodeConst)

        inner_cycle_list = self.module.ctx.HelperResolveSystemIdtf("inner_cycle_list", ScType.NodeConst)
        method_body = self.module.ctx.HelperResolveSystemIdtf("nrel_function_body", ScType.NodeConstNorole)
        cycle_body = self.module.ctx.HelperResolveSystemIdtf("nrel_iteration_body", ScType.NodeConstNorole)
        cycle = self.module.ctx.HelperResolveSystemIdtf("concept_cycle", ScType.NodeConstClass)

        method_find= self.module.ctx.Iterator5(class_find, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, method)

        while method_find.Next():
            method_body_find= self.module.ctx.Iterator5(method_find.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, method_body)
            iterate_method_body = self.module.ctx.Iterator5(method_body_find.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, ScType.NodeConstRole)
            while iiterate_method_body.Next():
                cycle_name = self.module.ctx.Iterator3(iterate_method_body.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConstClass)
                cycle_find = self.module.ctx.Iterator3(cycle_name.Get(2), ScType.EdgeAccessConstPosPerm, cycle)
                if cycle_find.IsValid():
                    cycle_body_find = self.module.ctx.Iterator5(iiterate_method_body.Get(2), ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, nrel_iteration_body)
                    iterate_cycle_body = self.module.ctx.Iterator5(cycle_body_find.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, ScType.NodeConstRole)
                    while iterate_cycle_body.Next():
                        inner_cycle_name = self.module.ctx.Iterator3(iterate_cycle_body.Get(2), ScType.EdgeAccessConstPosPerm, ScType.NodeConstClass)
                        inner_cycle_find = self.module.ctx.Iterator3(inner_cycle_name.Get(2), ScType.EdgeAccessConstPosPerm, cycle)
                        if inner_cycle_find.IsValid():
                            self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, inner_cycle_list,inner_cycle_find.Get(2))

        return ScResult.Ok

