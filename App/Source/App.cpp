#include <iostream>
#include "ECS/Entities.h"
#include <SDL.h>


int main(int argc, char* argv[])
{
   const int SCREEN_WIDTH = 640;
   const int SCREEN_HEIGHT = 480;

   SDL_Window* window = NULL;
   SDL_Surface* screenSurface = NULL;

   if (SDL_Init(SDL_INIT_VIDEO) < 0)
   {
      std::cout << "SDL could not initialize! SDL_Error: " << SDL_GetError();
   }

   SDL_Quit();

   Entities::PrintTest();
   return 0;
}
