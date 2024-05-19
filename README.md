# SDL Game Engine

## Using conan C dependency manager

0. Prerrequisites

- Have installed cmake.

1. Install conan python dist.

```
$ pip install conan
```

2. Create a conanfile.py where you can specify dependencies.

3. Create a default profile, based in your architecture and platform.

```
$ conan profile detect
```

**Note:** If the compiler that was detected is c++14 and you need to use the c++20, go to %USERPROFILE%\.conan2\profiles\default
and edit the file with the new compiler version.

4. Run Scripts\init.py to generate the dependencies files.

5. To use the dependencies that we have imported, you have to modify the Build.lua files in every project that you have. In this case, App and Core.

- App/Build.lua

``` lua
  filter "configurations:Dist"
       defines { "DIST" }
       runtime "Release"
       optimize "On"
       symbols "Off"

   conan_setup()
```

- Core/Build.lua

``` lua
   filter "configurations:Dist"
       defines { "DIST" }
       runtime "Release"
       optimize "On"
       symbols "Off"

   conan_setup()
```

6. After the modifications, run again Scripts\init.py

7. Open .sln file created.
