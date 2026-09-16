#include "module2.h"
#include "resource2.h"

static INT_PTR CALLBACK DialogProc2(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_INITDIALOG:
        return (INT_PTR)TRUE;

    case WM_COMMAND:
        if (LOWORD(wParam) == ID_NEXT_BTN)
        {
            EndDialog(hDlg, 1);
            return (INT_PTR)TRUE;
        }
        if (LOWORD(wParam) == ID_BACK_BTN)
        {
            EndDialog(hDlg, -1);
            return (INT_PTR)TRUE;
        }
        if (LOWORD(wParam) == IDCANCEL)
        {
            EndDialog(hDlg, 0);
            return (INT_PTR)TRUE;
        }
        break;

    case WM_CLOSE:
        EndDialog(hDlg, 0);
        return (INT_PTR)TRUE;
    }
    return (INT_PTR)FALSE;
}

int Func_MOD2_2(HWND hWnd)
{
    return (int)DialogBox(GetModuleHandle(NULL), MAKEINTRESOURCE(IDD_DIALOG2), hWnd, DialogProc2);
}