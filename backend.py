import winreg

DEFAULT_CONFIG = {"SteamPath" : "",
                  "InstallCSSTweaks" : "1",
                  "EnablePlayButtonBox" : "0",
                  "EnableVerticalNavBar" : "0",
                  "InstallWithDarkLibrary" : "0"}
user_config = {}

def find_library_dir():
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\Valve\Steam");
    steam_path = winreg.QueryValueEx(key, "SteamPath")[0]
    print(steam_path)
    steamui_path = steam_path.replace("/","\\") + "\steamui"
    print(steamui_path)



