' popup.vbs
Set WshShell = CreateObject("WScript.Shell")
Do
    response = MsgBox("Jesteś gówniarzem?", vbYesNo + vbQuestion, "Pytanie")
    If response = vbYes Then
        MsgBox "Wiedziałem!", vbInformation, "Sukces"
        Exit Do
    End If
Loop
WScript.Sleep 1800000 ' Czeka 30 minut (1800000 milisekund)
WshShell.Run WScript.ScriptFullName ' Uruchamia ponownie skrypt
