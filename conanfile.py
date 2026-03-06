from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout, CMakeDeps

class avltreeRecipe(ConanFile):
    name = "avltree"
    version = "1.0.0"
    author = "VirtualSelf intodarkblue@gmail.com"
    description = "Balanced Binary Search Tree - AVL"
    url = "https://github.com/NotVirtualSelf/AVLTree"
    settings = "os", "compiler", "build_type", "arch"
    
    options = {
        "shared": [True, False],
        "fPIC": [True, False]
    }
    default_options = {
        "shared": False,
        "fPIC": True
    }
    
    exports_sources = "CMakeLists.txt", "include/*"
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC
            
    def package_id(self):
        self.info.clear()

    def layout(self):
        cmake_layout(self)
    
    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        # cmake.build()
        
    def package_info(self):
        self.cpp_info.set_property("cmake_file_name", "AVLTree")
        self.cpp_info.set_property("cmake_target_name", "AVLTree::AVLTree")
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libs = []

    # This recipe is aimed at a consumer scenario. If you want to create
    # a package, then you should add the following attributes/methods:
    #   * exports_sources attribute (https://docs.conan.io/2/reference/conanfile/attributes.html#exports-sources)
    #   * package method (https://docs.conan.io/2/reference/conanfile/methods/package.html)
    #   * package_info method (https://docs.conan.io/2/reference/conanfile/methods/package_info.html)

