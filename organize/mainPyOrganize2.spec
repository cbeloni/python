# -*- mode: python -*-
a = Analysis(['mainPyOrganize2.py'],
             pathex=['/home/beloni/Documentos/PyProjects/organize'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='mainPyOrganize2',
          debug=False,
          strip=None,
          upx=True,
          console=True )
