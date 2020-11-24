
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (InnerCycleModule SHARED ${SOURCES})

target_include_directories(InnerCycleModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(InnerCycleModule sc-memory)

add_dependencies(InnerCycleModule sc-memory)

sc_codegen(InnerCycleModule ${CMAKE_CURRENT_LIST_DIR})
