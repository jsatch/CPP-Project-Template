include "Dependencies/conandeps.premake5.lua"

workspace "SDLGameEngine"
   architecture "x64"
   configurations { "Debug", "Release", "Dist" }
   startproject "App"

OutputDir = "%{cfg.system}-%{cfg.architecture}/%{cfg.buildcfg}"

group "Core"
	include "Core/Build-Core.lua"
group ""

include "App/Build-App.lua"
