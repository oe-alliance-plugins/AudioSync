from setuptools import setup
import setup_translate

pkg = 'Extensions.AudioSync'
setup(name='enigma2-plugin-extensions-audiosync',
       version='3.0',
       description='Set Audio delay',
       package_dir={pkg: 'AudioSync'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'img/*.png', 'AudioSync.png', 'LICENSE', 'maintainer.info', 'keymap.xml']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
