#include "ndModule.hpp"

SC_IMPLEMENT_MODULE(NoDiscardModule)

sc_result NoDiscardModule::InitializeImpl()
{
	m_hwService.reset(new NoDiscardAgentPythonService("NoDiscard/NoDiscardModule.py"));
	m_hwService->Run();
	return SC_RESULT_OK;
}

sc_result NoDiscardModule::ShutdownImpl()
{
	m_hwService->Stop();
	m_hwService.reset();
	return SC_RESULT_OK;
}
