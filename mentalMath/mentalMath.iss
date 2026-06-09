#define MyAppName "mentalMath"
#define MyAppVersion "1.0.0"
#define MyAppPublisher "mister anas "
#define MyAppURL "https://github.com/mesteranas/mentalMath_GUI/"
#define MyAppExeName "mentalMath.exe"

[Setup]
AppName={#MyAppName}
AppId={{41C9FB90-027C-4A17-9654-EF013B828EBF}}
AppVersion={#MyAppVersion }
;AppVersion={#MyAppVersion}
VersionInfoDescription=Mental Math GUI aims to make mental arithmetic training accessible, enjoyable, and efficient for blind and visually impaired users around the world.
AppPublisher={#MyAppPublisher }
VersionInfoVersion={#MyAppVersion}
VersionInfoCompany={#MyAppPublisher }
VersionInfoCopyright=copyright, ©2026 Mister Anas
VersionInfoProductName=mentalMath
VersionInfoProductVersion={#MyAppVersion}
VersionInfoOriginalFileName=mentalMath_Setup.exe
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
ArchitecturesAllowed=x64
DefaultDirName={sd}\program files\{#MyAppName}
DisableProgramGroupPage=yes
PrivilegesRequired=admin
OutputDir=mentalMath_build
OutputBaseFilename=mentalMathSetup
LicenseFile=data\help\LICENSE.txt
Compression=lzma
CloseApplications=force
restartApplications=yes
SolidCompression=yes
WizardStyle=modern
DisableWelcomePage=no

ArchitecturesInstallIn64BitMode=x64
MinVersion=0,6.2
[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
[CustomMessages]
english.DeleteDataPrompt=Do you want to delete app settings' files?

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"
[Files]
Source: "mentalMath_build\{#MyAppExeName}"; DestDir: "{app}"; Flags: ignoreversion
Source: "mentalMath_build\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{autoprograms}\mentalMath"; Filename: "{app}\{#MyAppExeName}"; 
Name: "{autodesktop}\mentalMath"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[UninstallRun]
Filename: "taskkill"; Parameters: "/F /IM mentalMath.exe"; Flags: runhidden

[UninstallDelete]
Type: filesandordirs; Name: "{pf}\mentalMath"

[InstallDelete]
Type: filesandordirs; Name: "{app}\*"

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall

[Code]
function InitializeSetup(): Boolean;
begin
  Result := True;
end;


procedure CurStepChanged(CurStep: TSetupStep);
begin
end;

procedure DeleteSettingsFolder();
begin
  DelTree(ExpandConstant('{userappdata}\mentalMath_GUI'), True, True, True);
end;

function AskDeleteSettingsFolder(): Boolean;
begin
  Result := MsgBox(ExpandConstant('{cm:DeleteDataPrompt}'), mbConfirmation, MB_YESNO) = IDYES;
end;

procedure CurUninstallStepChanged(CurUninstallStep: TUninstallStep);
begin
  if CurUninstallStep = usUninstall then
  begin
    if AskDeleteSettingsFolder() then
    begin
      DeleteSettingsFolder();
    end;
  end;
end;

