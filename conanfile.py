from conan import ConanFile

class ConanDependencyConfig(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "PremakeDeps"

    def requirements(self):
        self.requires("spdlog/1.14.1")
        self.requires("sdl/2.30.3")
