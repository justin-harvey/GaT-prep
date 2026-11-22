#!/usr/bin/env bash
# Brain Blasters: install as an offline app for the current Linux user.
# No internet or sudo needed. Run from the downloaded repository folder:
#     bash linux/install.sh              install or update
#     bash linux/install.sh --uninstall  remove (saved progress stays in the browser)
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SRC="$HERE/../index.html"
# A visible folder in your home directory, so sandboxed (snap) browsers can open it too.
APPDIR="$HOME/BrainBlasters"
BINDIR="$HOME/.local/bin"
DATA="${XDG_DATA_HOME:-$HOME/.local/share}"
DESKDIR="$DATA/applications"
ICONDIR="$DATA/icons/hicolor/scalable/apps"

if [ "${1:-}" = "--uninstall" ]; then
  rm -f "$APPDIR/index.html" "$BINDIR/brain-blasters" "$DESKDIR/brain-blasters.desktop" "$ICONDIR/brain-blasters.svg"
  rmdir "$APPDIR" 2>/dev/null || true
  command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$DESKDIR" >/dev/null 2>&1 || true
  echo "Brain Blasters was removed."
  exit 0
fi

if [ ! -f "$SRC" ]; then
  echo "Couldn't find index.html. Run this script from inside the downloaded Brain Blasters folder." >&2
  exit 1
fi

mkdir -p "$APPDIR" "$BINDIR" "$DESKDIR" "$ICONDIR"
cp "$SRC" "$APPDIR/index.html"
cp "$HERE/brain-blasters.svg" "$ICONDIR/brain-blasters.svg"

cat > "$BINDIR/brain-blasters" <<'LAUNCHER'
#!/usr/bin/env bash
# Opens Brain Blasters offline, in its own app window when the browser supports it.
URL="file://$HOME/BrainBlasters/index.html"
for b in brave-browser brave brave-browser-stable google-chrome google-chrome-stable chromium chromium-browser microsoft-edge vivaldi; do
  if command -v "$b" >/dev/null 2>&1; then exec "$b" --app="$URL" --class=BrainBlasters; fi
done
if command -v firefox >/dev/null 2>&1; then exec firefox --new-window "$URL"; fi
exec xdg-open "$URL"
LAUNCHER
chmod +x "$BINDIR/brain-blasters"

cat > "$DESKDIR/brain-blasters.desktop" <<DESKTOP
[Desktop Entry]
Type=Application
Name=Brain Blasters
Comment=Comic-book puzzle practice for the CogAT (works offline)
Exec=$BINDIR/brain-blasters
Icon=brain-blasters
Terminal=false
Categories=Education;Game;
StartupWMClass=BrainBlasters
DESKTOP
chmod +x "$DESKDIR/brain-blasters.desktop"

command -v update-desktop-database >/dev/null 2>&1 && update-desktop-database "$DESKDIR" >/dev/null 2>&1 || true
command -v gtk-update-icon-cache >/dev/null 2>&1 && gtk-update-icon-cache -q -t "$DATA/icons/hicolor" >/dev/null 2>&1 || true

echo "Brain Blasters is installed."
echo "  Open it from your app menu (look for \"Brain Blasters\"), or run: $BINDIR/brain-blasters"
echo "  The game file is in: $APPDIR/index.html"
