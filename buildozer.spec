[app]
title = BirthdayApp
package.name = birthdayapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3==3.10.12,kivy==2.3.0,kivymd==1.2.0
orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.presplash_color = white
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
p4a.branch = master
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
