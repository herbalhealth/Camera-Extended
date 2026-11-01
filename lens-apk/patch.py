p='android/app/src/main/AndroidManifest.xml'
s=open(p).read()
perms='''<uses-permission android:name="android.permission.CAMERA"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS"/>
    <uses-feature android:name="android.hardware.camera" android:required="false"/>
'''
open(p,'w').write(s.replace('</manifest>',perms+'</manifest>'))
