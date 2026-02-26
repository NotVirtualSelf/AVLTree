cmake_minimum_required(VERSION 3.10)
project(AVLtree VERSION 1.0.0 LANGUAGES CXX)

add_library(${PROJECT_NAME} INTERFACE)

target_include_directories(${PROJECT_NAME} INTERFACE
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
    $<INSTALL_INTERFACE:include/${PROJECT_NAME}>
)

install(DIRECTORY include/
    DESTINATION include/${PROJECT_NAME}
    FILES_MATCHING PATTERN "*.h" PATTERN "*.inl"
)

install(TARGETS ${PROJECT_NAME} EXPORT ${PROJECT_NAME}Config)

install(EXPORT ${PROJECT_NAME}Config
    DESTINATION lib/cmake/${PROJECT_NAME}
)

target_compile_features(${PROJECT_NAME} INTERFACE cxx_std_14)