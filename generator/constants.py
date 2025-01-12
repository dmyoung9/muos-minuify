from generator.utils import find_base_dirs


BASE_DIR, RESOURCES_DIR = find_base_dirs()

ASSETS_DIR = BASE_DIR / "Assets"
FONTS_DIR = ASSETS_DIR / "Font"
GLYPHS_DIR = ASSETS_DIR / "glyphs"
HORIZONTAL_LOGOS_DIR = ASSETS_DIR / "Horizontal Logos"
BUTTON_GLYPHS_DIR = ASSETS_DIR / "Button Glyphs"
OVERLAY_DIR = ASSETS_DIR / "Overlays"
TEMPLATE_SCHEME_DIR = BASE_DIR / "Template Scheme"
TEMPLATE_SCHEME_FILENAME = "template.txt"
TEMPLATE_SCHEME_PATH = TEMPLATE_SCHEME_DIR / TEMPLATE_SCHEME_FILENAME
THEME_SHELL_DIR = BASE_DIR / "Theme Shell"

CONFIG_FILENAME = "MinUIThemeGeneratorConfig.json"
CONFIG_PATH = BASE_DIR / CONFIG_FILENAME

PREMADE_THEMES_FILENAME = "PremadeThemes.json"
PREMADE_THEMES_PATH = BASE_DIR / PREMADE_THEMES_FILENAME
