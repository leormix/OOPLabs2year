#include <windows.h>
#include "module1.h"

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow)
{
    int result = Func_MOD2_1(NULL);

    if (result == 1)
    {
        MessageBoxW(NULL, L"Натиснуто: Next >", L"Результат", MB_OK | MB_ICONINFORMATION);
    }
    else
    {
        MessageBoxW(NULL, L"Натиснуто: Cancel", L"Результат", MB_OK | MB_ICONWARNING);
    }

    return 0;
}