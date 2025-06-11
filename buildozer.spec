[app]
title = CookMaster
package.name = cookmaster
package.domain = org.cookmaster
source.dir = .
source.include_exts = py,png,jpg,kv
version = 1.0
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.archs = arm64-v8a
android.ndk_api = 21
android.private_storage = true
icon.filename = %(source.dir)s/data/icon.png
presplash.filename = %(source.dir)s/data/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
