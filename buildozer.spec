[app]

# (str) Title of your application
title = CookMaster

# (str) Package name
package.name = cookmaster

# (str) Package domain (unique, like a reverse URL)
package.domain = org.yourname

# (str) Source code entry point
source.main = main.py

# (list) Source files to include (add all your .py files here)
source.include_exts = py,png,jpg,kv,json

# (str) Application versioning
version = 1.0

# (list) Permissions
android.permissions = INTERNET

# (str) Icon path (optional, use .png format)
# icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation (portrait, landscape, etc.)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Application requirements
# Add kivy and any other dependencies
requirements = python3,kivy

# (str) Android NDK version (you can leave this default)
android.ndk = 25b

# (str) Android API level to build with
android.api = 33

# (str) Android SDK version
android.sdk = 33

# (bool) Copy the .apk to the current directory
copy_to_current_dir = 1

# (str) Output filename
android.archs = armeabi-v7a, arm64-v8a
