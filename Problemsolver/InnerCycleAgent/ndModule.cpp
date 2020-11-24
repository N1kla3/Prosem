#include "ndModule.hpp"

SC_IMPLEMENT_MODULE(InnerCycleModule)

sc_result InnerCycleAgentModule::InitializeImpl()
{
	m_hwService.reset(new InnerCycleAgentPythonService("InnerCycleAgent/InnerCycleModule.py"));
	m_hwService->Run();
	return SC_RESULT_OK;
}

sc_result InnerCycleAgentModule::ShutdownImpl()
{
	m_hwService->Stop();
	m_hwService.reset();
	return SC_RESULT_OK;
}
