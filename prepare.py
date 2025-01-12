import os, shutil, site

sitedir = None
if hasattr(site, 'getsitepackages'):
    # normal execution
    sitepackages = site.getsitepackages()
    sitedir = sitepackages[0]
else:
    # workaround for virtualenv
    from distutils.sysconfig import get_python_lib
    sitepackages = [get_python_lib()]
    sitedir = sitepackages[0]
install_pkg_dir = os.path.join(sitedir, 'bbc1')
target_dir = os.path.join(install_pkg_dir, 'libs')
os.makedirs(target_dir, exist_ok=True)
if os.path.exists('bbc1/libs/libbbcsig.so'):
    dst_path = os.path.join(target_dir, 'libbbcsig.so')
    shutil.copy('bbc1/libs/libbbcsig.so', dst_path)
elif os.path.exists('bbc1/libs/libbbcsig.dylib'):
    dst_path = os.path.join(target_dir, 'libbbcsig.dylib')
shutil.copy('bbc1/libs/libbbcsig.dylib', dst_path)
