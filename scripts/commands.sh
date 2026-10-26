# Command reference only. Copy individual examples; never execute/source this file.
# Shell examples: Bash in the project root on WINDOWS (e.g. Git Bash), using native Windows Python.
# WSL/Linux Python is NOT supported: keyboard.py accesses ctypes.windll.user32.SendInput.
# Console examples are comments: copy the text WITHOUT "# " into Sound Manager, not Bash.
# Prerequisites: Poetry and Python >=3.10,<4.0 (manifest supersedes README's Python 3.5).
# poetry.lock records Python ^3.11 despite the manifest's ^3.10; use Python 3.11+.
# Lock freshness has not been runtime-verified; if Poetry rejects it, reconcile separately.
# Install the local package and cmd2 dependency.
poetry install

# Launch the interactive console; no console-script entry point or project argparse flags exist.
# It emulates Windows media keys for the default audio device, not per-application mixer settings.
poetry run python -m sound_manager.api_console

# --- Commands INSIDE the running console ---
# List command help or inspect volume_set's positional integer argument.
# help
# help volume_set

# Inspect INTERNAL tracking only, not the actual Windows mixer state.
# Before the first mutation this reports volume 0 and muted False regardless of the OS state.
# External volume changes are not tracked.
# status

# IMPORTANT: the FIRST mutating command sends 50 volume-up key events (maximum volume)
# BEFORE applying the requested action. Even volume_min, mute, or volume_set 20 can
# briefly raise volume to maximum. Stop audio playback and protect hearing/equipment first.
# No dry-run, device selection, confirmation, or reliable OS-state readback is implemented.

# Toggle mute/unmute; this is not an idempotent "mute on" command.
# mute

# Increase or decrease the tracked level by two; both emit real Windows key events.
# volume_up
# volume_down

# Set an even level in 0..100; odd inputs are rounded by the two-step implementation.
# Keep inputs in range: argparse accepts any integer and does not enforce these bounds.
# volume_set 20

# Alternatives: minimum or maximum volume (maximum may be dangerously loud).
# volume_min
# volume_max

# Clear the terminal or exit; quit is explicitly implemented by this console.
# clear
# quit

# No nonempty tests, lint configuration, deployment, or publishing workflow is defined.
# Windows audio behavior has NOT been runtime-tested by this catalogue's static validation.
