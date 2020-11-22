
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (ShteinModule SHARED ${SOURCES})

target_include_directories(ShteinModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(ShteinModule sc-memory)

add_dependencies(ShteinModule sc-memory)

sc_codegen(ShteinModule ${CMAKE_CURRENT_LIST_DIR})
