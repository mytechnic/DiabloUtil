# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(['C:/App/Project/DiabloUtil/DiabloCloneStarHunterMaster.py'],
             pathex=[],
             binaries=[],
             datas=[('C:/App/Project/DiabloUtil/README.txt', '.'), ('C:/App/Project/DiabloUtil/star.png', '.')],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=True,
             win_private_assemblies=True,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts, 
          [],
          exclude_binaries=True,
          name='DiabloCloneStarHunterMaster',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None , icon='C:\\App\\Project\\DiabloUtil\\star.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas, 
               strip=False,
               upx=True,
               upx_exclude=[],
               name='DiabloCloneStarHunterMaster')
