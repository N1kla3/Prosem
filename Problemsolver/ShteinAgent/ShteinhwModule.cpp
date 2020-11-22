/*
* This source file is part of an OSTIS project. For the latest info, see http://ostis.net
* Distributed under the MIT License
* (See accompanying file COPYING.MIT or copy at http://opensource.org/licenses/MIT)
*/

#include "ShteinhwModule.hpp"

SC_IMPLEMENT_MODULE(ShteinAgentModule)

sc_result ShteinAgentModule::InitializeImpl()
{
  m_hwService.reset(new ShteinAgentPythonService("ShteinAgent/ShteinModule.py"));
  m_hwService->Run();
  return SC_RESULT_OK;
}

sc_result ShteinAgentModule::ShutdownImpl()
{
  m_hwService->Stop();
  m_hwService.reset();
  return SC_RESULT_OK;
}
