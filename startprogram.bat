@echo off
title FNAPI 1.3 (BETA)
if not exist "Maps" (
    mkdir "Maps"
)

if not exist "Paks" (
    mkdir "Paks"
)

if not exist "Mnemonic" (
    mkdir "Mnemonic"
)

if not exist "Mappings" (
    mkdir "Mappings"
)

if not exist "Lobby" (
    mkdir "Lobby"
)
if not exist "Exports" (
    mkdir "Exports"
)
if not exist "News" (
    mkdir "News"
)
py bot.py
