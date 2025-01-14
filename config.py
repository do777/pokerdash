# parameters for the Elo algorithm -- setting kind of arbitrarily for now, should tune once we have more data
DEFAULT_K_VALUE = 32
DEFAULT_D_VALUE = 400
DEFAULT_SCORING_FUNCTION_BASE = 1.25
INITIAL_RATING = 1000

# Google Sheets info for reading input data
GSHEETS_CREDENTIALS_FILE = "./google-credentials.json"
SPREADSHEET_ID = "1CXQVBTvWmkon5vkuAGdPVSKs373ZqK3_XTqi3dJF7dM"
DATA_SHEET_ID = 839670511
DUMMY_PLAYER_NAME = "_dummy_"

# dashboard settings
DBC_THEME = "FLATLY"  # others I liked: DARKLY, SIMPLEX, LUMEN (https://bootswatch.com/flatly/)
PLOTLY_THEME = "plotly_white"
LOGO_PATH = "/assets/Red-Dog-Txt-&-Logo.jpg"
GITHUB_LOGO_PATH = "assets/GitHub-Mark-32px.png"
GITHUB_URL = "https://github.com/djcunningham0/poker-elo"
TITLE = "문래 포커 클럽"
SUBTITLE = "home of honest poker"
