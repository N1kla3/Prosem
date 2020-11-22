
file(GLOB_RECURSE SOURCES "*.cpp" "*.hpp")

add_library (vadimModule SHARED ${SOURCES})

target_include_directories(vadimModule PRIVATE ${SC_MEMORY_SRC})
target_link_libraries(vadimModule sc-memory)

add_dependencies(vadimModule sc-memory)

sc_codegen(vadimModule ${CMAKE_CURRENT_LIST_DIR})
