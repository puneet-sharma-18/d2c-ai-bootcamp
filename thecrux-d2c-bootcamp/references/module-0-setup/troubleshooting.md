# Module 0 Troubleshooting

The five most common install issues, with fixes. TAs and founders both reference this. If your issue is not here, raise hand and a TA pairs in.

## 1. `claude: command not found` after install

**Cause.** Claude Code installed but not on your PATH.

**Fix.**

```bash
# Find where npm puts global bins
npm prefix -g

# That output, plus /bin, is the path. Add it to your shell rc.
# For zsh (macOS default):
echo 'export PATH="$(npm prefix -g)/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc

# For bash:
echo 'export PATH="$(npm prefix -g)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

If you installed via homebrew on macOS:

```bash
brew reinstall claude-code
```

If you installed via curl:

```bash
# Re-run the install script. It usually fixes the PATH.
curl -fsSL https://claude.ai/install.sh | sh
```

## 2. `claude` runs but asks for API key every time

**Cause.** Not logged in.

**Fix.**

```bash
claude login
```

Opens a browser flow. Sign in with your Anthropic account. Returns to terminal with a confirmation. Done.

If you have an API key directly (paid plan, or your team gave you one):

```bash
# macOS / Linux
echo 'export ANTHROPIC_API_KEY="sk-ant-..."' >> ~/.zshrc
source ~/.zshrc

# Then verify
claude
```

## 3. Cannot clone the repo

**Cause.** Either no git installed, or no GitHub access, or SSH not set up.

**Fix.**

If git is not installed:

```bash
# macOS
xcode-select --install

# Ubuntu / Debian
sudo apt-get install git

# Windows (in PowerShell)
winget install Git.Git
```

If git is installed but `git clone` fails with permission errors:

```bash
# Use HTTPS, not SSH
git clone https://github.com/thecrux-ai/thecrux-d2c-bootcamp.git
```

If even HTTPS fails:

1. Open the repo in your browser
2. Click "Code" -> "Download ZIP"
3. Unzip into a folder named `thecrux-d2c-bootcamp`
4. `cd` into it

## 4. Windows: WSL issues

**Cause.** Claude Code on Windows runs best inside WSL2 (Windows Subsystem for Linux). Founders who installed Claude Code on the Windows side instead of inside WSL hit weird issues with file paths, shell scripts and MCPs.

**Fix.**

```powershell
# In PowerShell, confirm WSL2 is running:
wsl --status

# If WSL is not installed:
wsl --install

# Reboot, then open Ubuntu (or the WSL distro you chose).
# Inside WSL:
curl -fsSL https://claude.ai/install.sh | sh
```

From now on, do all workshop work inside WSL, not in PowerShell or CMD.

## 5. Founder has Claude Desktop but never used CLI

**Cause.** Claude Desktop and Claude Code (the CLI) are separate installs. Having Desktop does not give you the CLI.

**Fix.** Install Claude Code now:

```bash
# macOS (homebrew)
brew install claude-code

# macOS / Linux (npm)
npm install -g @anthropic-ai/claude-code

# Windows (inside WSL)
npm install -g @anthropic-ai/claude-code
```

Verify:

```bash
claude --version
```

Should print a version. Then `claude login` if needed (see issue 2).

## 6. Repo opens but Claude says "I don't have access to read these files"

**Cause.** Founder ran `claude` from the wrong directory, or the repo is in a path Claude cannot access (e.g. iCloud Drive on macOS sometimes blocks).

**Fix.**

```bash
# Move the repo to a plain local folder
mv ~/Library/Mobile\ Documents/com~apple~CloudDocs/thecrux-d2c-bootcamp ~/thecrux-d2c-bootcamp
cd ~/thecrux-d2c-bootcamp
claude
```

Then ask Claude again:

```
List the files in this directory.
```

If it still says no access, exit and re-enter:

```bash
exit  # leave Claude
cd ~/thecrux-d2c-bootcamp
claude
```

## 7. Terminal looks weird, fonts cut off, colours wrong

**Cause.** Terminal app or font config.

**Fix.** Out of scope for the workshop. We work with whatever terminal you have. If the rendering is genuinely unreadable, switch to:

- macOS: iTerm2 (free)
- Windows: Windows Terminal (preinstalled on Windows 11) inside WSL
- Linux: GNOME Terminal or Konsole, both fine

Do not spend Module 0 tweaking fonts. Cosmetic. Move on.

## When in doubt

Raise hand. A TA pairs in within 60 seconds. The cohort goal is everyone at Module 1 starting on time. Anything blocking that is a pairing job, not a "founder figures it out alone" job.
