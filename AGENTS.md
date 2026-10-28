# Project agent instructions

## Required project-file download before MCP use

Before starting, connecting to, or calling any MCP server for this project, first download and fully materialize all project files required for the task to the local filesystem. This includes files tracked through Git submodules and Git LFS. Do not use the MCP until the downloads have completed successfully and the required files are present locally. If authentication, missing files, or another issue prevents a complete download, stop and report what is unavailable instead of proceeding with the MCP.

## Project layout

This repository is the central workspace for DAZ Studio projects and asset production. `Scene ABFD/` contains the DAZ scenes. `Assert ABFD/` is the library of assets we create, such as characters and locations. The other top-level DAZ content folders are working/source libraries used to build our assets, which are then used in scenes; do not confuse these source folders with the scenes themselves. Many top-level folders are Git submodules. `docs/` contains the Markdown documentation for the project assets across the libraries; use `docs/_Sidebar.md` as its index and consult the relevant asset page when working with an asset. `mcp-server/` contains the DAZ MCP server and its supporting files. `Bozze/` is the local holding area for assets still in draft. Its contents are intentionally excluded from Git and should not be committed.

## Use DAZ Studio Formats for DAZ assets

For DAZ asset discovery, browsing, loading, saving, and path resolution, always use the directories registered under **DAZ Studio Formats** in DAZ Studio. Do not assume every project folder is a content library or substitute Poser Formats. Treat DAZ Studio's live content manager list as the authoritative source; the local `ContentDirectoryManager.dsx` was found empty while DAZ Studio had active directories configured, so do not rely on that file alone.

### Get the active DAZ Studio Formats directory list

After completing the required project-file downloads above, call the DAZ MCP `daz_execute` tool with this read-only DazScript:

```javascript
(function(){
    var cm = App.getContentMgr();
    var dirs = [];
    for (var i = 0; i < cm.getNumContentDirectories(); i++) {
        var dir = cm.getContentDirectory(i);
        if (dir) dirs.push(String(dir.fullPath));
    }
    return dirs;
})()
```

Use the returned paths for DAZ content operations. The list currently includes the project libraries under `D:\DAZ 3D`, including `Bozze` for draft assets. Re-query it from the live content manager when accuracy matters, because the configured list can change.

### Start DAZ Studio before using its MCP during scene creation

For scene creation, first complete the required-file download/materialization checks above. Then start DAZ Studio from the terminal using the command below, or verify that it is already running. Do this before the first DAZ MCP call so its MCP server is ready for the scene workflow. Do not probe the DAZ MCP first to see whether Studio is running; use the process check below instead.

## Diagnose missing asset dependencies

If a DAZ asset fails to load or reports missing geometry, UV sets, morphs, textures, or other linked files, do a brief local investigation to identify the connected product/library before continuing:

1. Record the exact unresolved resource paths from the DAZ log or MCP error. Do not repeatedly retry the same incomplete preset.
2. Check the asset's DAZ file and `asset_id`, consult the relevant page in `docs/` using `docs/_Sidebar.md`, and search the active DAZ Studio Formats folders for the referenced files.
3. Search online for a few exact, distinctive fragments from the unresolved paths (for example, `hameleon LivingRoom2 SmartphoneL Smartphone.dsf` or `Lr2SmartphoneDisplay.jpg`). Prefer the product's documentation, the vendor page, and the matching project repository to identify which related product/asset should contain the files. Copy the paths from the DAZ log rather than relying on user-typed examples, which may contain transcription errors.
4. Check whether the likely source submodule is initialized and whether the referenced files are tracked, ignored, missing, or still Git LFS pointers. Do not overwrite or reset local changes while investigating.
5. Tell the user briefly which linked asset/library is incomplete, what evidence identifies it, and the exact missing resource paths. If the required files are not fully available locally, stop all further MCP calls until the files have been downloaded and verified; do not substitute a guessed product or continue with a partial asset. Do not install or download third-party content unless the user asks.

### Camera and lighting groups

Scene camera/light rigs must be loaded from the **Lights HDRI** library, using the preset `D:/DAZ 3D/Lights HDRI/ATK Fantastic Lights 04.duf` (relative content path: `Lights HDRI/ATK Fantastic Lights 04.duf`). Do not use a camera bundled with the environment. Each loaded rig is one DAZ group containing a camera and its three-point lights. Add rigs one at a time, and keep only the selected camera rig group visible; hiding a rig group also hides its lights. In scene-building workflows, create at least three rigs with distinct views of the same scene. If an example image is provided, make the first camera approximate its framing before adding the other views.

### Screenshot storage and cleanup

All screenshots captured or generated during work, across every project and application, use the same temporary-file process. Save them outside project folders under `%TEMP%/DAZ-Scene-Previews/<task-or-project-name>/`, so they do not mix with drafts or get committed accidentally. The Windows scheduled task `DAZ Scene Preview Cleanup` removes screenshot files older than 14 days daily; its script is `%LOCALAPPDATA%/DAZ 3D/Cleanup-Scene-Previews.ps1`. Apply this to every screenshot, not only DAZ viewport captures.

### Iterative visual review

For visual work in any application, verify progress with the lightest useful method. Prefer an app's direct preview or a screenshot cropped to the relevant canvas, viewport, camera frame, or result area; avoid capturing the whole desktop when surrounding UI does not help evaluate the work. Use structured/app data for measurable state when available, and screenshots for visual qualities such as composition, pose, legibility, and framing. Save all captures using the temporary screenshot process above.

When a visual draft reaches a meaningful checkpoint, send the user a provisional screenshot even if it is not final, inspect it, identify visible issues, correct them, and repeat the capture-and-review cycle until the result is reasonably clear and coherent. For scene work, always do this after posing is established and cameras are set, then share the revised views as needed while correcting problems. Do not wait for final delivery to show the first visual preview. A successful capture or render command alone does not prove the image is useful; inspect the captured content.

For DAZ scene creation or modification, inspect the installed pose's thumbnail/reference image before applying it, compare it with the planned action and character, and send that pose preview to the user with a short explanation of why it fits. If the applied pose proves clearly unsuitable or causes repeated problems, reassess it rather than forcing it: look for another compatible installed pose, then search online if the local library has no good option, and propose the replacement to the user. Follow the external-content installation rule in the scene procedure. During intermediate scene review inspect screenshots of DAZ Studio's viewport, not Iray renders. Do not launch Iray renders for intermediate previews. Launch final renders or a render queue only when the user requests them, following `docs/Procedure-Render-Queue.md`.

For image-based pose retargeting or a pose-solver workflow, follow this order: select a suitable local pose or find an online candidate, send its preview image or link to the user, apply it as a rough body pose and place/orient the character on the intended surface, then set the camera to approximate the reference image. Only after these setup stages should detailed pose solving or calibration begin. Keep solver calibration separate from final scene editing; never save a test change to the scene unless the user asks.

## Workflow procedures

Follow the relevant step-by-step workflow in `docs/`:

- [Create a scene, edit posing, and complete the scene](docs/Procedure-Scene-Posing-Completion.md)
- [Start a render or render queue](docs/Procedure-Render-Queue.md)
- [Add an asset to our asset library](docs/Procedure-Add-Asset.md)

## Maintain project procedures and instructions

During project work, update the relevant Markdown procedure and `AGENTS.md` when the user clarifies a convention or when a workflow sequence has been verified. Keep project-wide rules and conventions in `AGENTS.md`; keep task-specific steps in the relevant procedure file. This maintenance rule applies across all project workflows, not only DAZ scene creation.

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
