# Project agent instructions

## Required project-file download before MCP use

Before starting, connecting to, or calling any MCP server for this project, first download and fully materialize all project files required for the task to the local filesystem. This includes files tracked through Git submodules and Git LFS. Do not use the MCP until the downloads have completed successfully and the required files are present locally. If authentication, missing files, or another issue prevents a complete download, stop and report what is unavailable instead of proceeding with the MCP.

## Project layout

This repository is the central workspace for DAZ Studio projects. Most top-level folders are individual DAZ projects or asset collections; many are Git submodules. `docs/` contains project documentation, and `mcp-server/` contains the DAZ MCP server and its supporting files. `Bozze/` is the local holding area for DAZ assets that are still drafts. Its contents are intentionally excluded from Git and should not be committed.

## Open DAZ Studio 4 from the terminal

DAZ Studio 4.24 is installed at `C:\DAZ\Applications\64-bit\DAZ 3D\DAZStudio4\DAZStudio.exe`. In PowerShell, start it with:

```powershell
$dazExe = 'C:\DAZ\Applications\64-bit\DAZ 3D\DAZStudio4\DAZStudio.exe'
Start-Process -FilePath $dazExe -WorkingDirectory (Split-Path -Parent $dazExe)
```

Use the executable's containing directory as the working directory. The same executable can be launched from CMD with:

```cmd
start "" /D "C:\DAZ\Applications\64-bit\DAZ 3D\DAZStudio4" "C:\DAZ\Applications\64-bit\DAZ 3D\DAZStudio4\DAZStudio.exe"
```

## Close DAZ Studio 4 from the terminal

Prefer a graceful close so DAZ Studio can prompt to save unsaved work. In PowerShell:

```powershell
Get-Process DAZStudio -ErrorAction SilentlyContinue | ForEach-Object { [void]$_.CloseMainWindow() }
```

Check whether it has exited before continuing:

```powershell
Get-Process DAZStudio -ErrorAction SilentlyContinue
```

Only if it is unresponsive and after confirming there is no unsaved work to preserve, force close it with:

```powershell
Stop-Process -Name DAZStudio -Force
```

In CMD, request a normal close with:

```cmd
taskkill /IM DAZStudio.exe
```
