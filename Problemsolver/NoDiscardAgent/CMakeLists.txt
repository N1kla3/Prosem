
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (NoDiscardModule SHARED ${SOURCES})

target_include_directories(NoDiscardModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(NoDiscardModule sc-memory)

add_dependencies(NoDiscardModule sc-memory)

sc_codegen(NoDiscardModule ${CMAKE_CURRENT_LIST_DIR})
