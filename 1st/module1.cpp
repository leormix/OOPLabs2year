#include "module1.h"
#include "resource1.h"

// hdlg окно, message (закрыли открыли там) wParam та lParam детали (номер кнопки и тд)
// INT_PTR указывает винде что это функция для обработки окна

static INT_PTR CALLBACK DialogProc1(HWND hDlg, UINT message, WPARAM wParam, LPARAM lParam)
{
    switch (message)
    {
    case WM_INITDIALOG:       // Инит окна в памяти
        return (INT_PTR)TRUE; // Ответ винде какой-то там блять что за шифры

    case WM_COMMAND:
        if (LOWORD(wParam) == ID_NEXT_BTN)
        {
            EndDialog(hDlg, 1);
            return (INT_PTR)TRUE; // Обозначение конца функции (зачем оно вообще ദ്ദി ༎ຶ‿༎ຶ ))
        };
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
    return (INT_PTR)FALSE; // На случай если взорвался ядерный реактор
}

int Func_MOD2_1(HWND hWnd)
{
    return (int)DialogBox(GetModuleHandle(NULL), MAKEINTRESOURCE(IDD_DIALOG1), hWnd, DialogProc1);
};

// Dialog box - creating modal window
