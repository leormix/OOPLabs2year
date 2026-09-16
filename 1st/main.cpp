#include <windows.h>
#include "module1/module1.h"
#include "module2/module2.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    int step = 1;

    while (step > 0)
    {
        if (step == 1)
        {
            int res = Func_MOD2_1(NULL);
            if (res == 1)
            {
                step = 2;
            }
            else
            {
                break;
            }
        }

        else if (step == 2)
        {
            int res = Func_MOD2_2(NULL);
            if (res == 1)
            {
                MessageBoxW(NULL, L"We're so fcking going", L"OK", MB_OK | MB_ICONINFORMATION);
                break;
            }
            else if (res == -1)
            {
                step = 1;
            }
            else
            {
                break;
            };
        };
    };

    return 0;
}