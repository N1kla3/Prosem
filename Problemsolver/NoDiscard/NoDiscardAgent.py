from common import ScModule, ScAgent, ScEventParams
from sc import *

class NoDiscardAgent(ScAgent):


    def RunImpl(self, evt: ScEventParams) -> ScResult: 
        print("NoDiscardAgent : RunImpl")
        codeblock = evt.other_addr
        check_functions = self.module.ctx.HelperResolveSystemIdtf("nodiscard_check_functions", ScType.NodeConstClass)
        method = self.module.ctx.HelperResolveSystemIdtf("concept_called_method", ScType.NodeConstClass)
        answer = self.module.ctx.HelperResolveSystemIdtf("NoDiscardAnswer", ScType.NodeConst)
        if answer.IsValid():
            print("answer valid")

        iterate_code_block = self.module.ctx.Iterator5(codeblock, ScType.EdgeAccessConstPosPerm, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, ScType.NodeConstRole)
        while iterate_code_block.Next():
            print("sss")
            iterate_methods = self.module.ctx.Iterator3(method, ScType.EdgeAccessConstPosPerm, iterate_code_block.Get(2))
            iterate_methods.Next()
            if iterate_methods.IsValid():
                self.module.ctx.CreateEdge(ScType.EdgeAccessConstPosPerm, check_functions, iterate_methods.Get(2))
        iterate_checks = self.module.ctx.Iterator3(check_functions, ScType.EdgeAccessConstPosPerm, ScType.NodeConst)
        while iterate_checks.Next():
            print("dsfsdf")
            node = iterate_checks.Get(2) 
            void = self.module.ctx.HelperResolveSystemIdtf("concept_void", ScType.NodeConst)
            func_proto = self.module.ctx.HelperResolveSystemIdtf("nrel_function_prototype", ScType.NodeConstNoRole)
            find_prototype = self.module.ctx.Iterator5(node, ScType.EdgeDCommonConst, ScType.NodeConst, ScType.EdgeAccessConstPosPerm, func_proto) 
            find_prototype.Next()
            if find_prototype.IsValid():
                check_type = self.module.ctx.Iterator5(find_prototype.Get(2), ScType.EdgeDCommonConst, ScType.NodeConstClass, ScType.EdgeAccessConstPosPerm, ScType.NodeConstNoRole) 
                check_type.Next()
                if check_type.IsValid():
                    type = check_type.Get(2)
                    if type.IsValid():
                        print("type valid")
                    if type != void:
                        if type.IsValid():
                            print("type valid")
                        edge = self.module.ctx.CreateEdge(ScType.EdgeAccess, answer, iterate_checks.Get(2))
                        if edge.IsValid():
                            print("create")
        self.module.ctx.DeleteElement(check_functions)
        return ScResult.Ok

