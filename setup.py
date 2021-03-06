from setuptools import setup

setup(
    name="popupdict",
    version="0.1.2",
    packages=['popupdict'],
    include_package_data=True,
    zip_safe=True,

    author='Bian Jiaping',
    author_email='ssbianjp@gmail.com',
    url='https://github.com/bianjp/popup-dict',
    license='MIT',

    keywords='dict youdao',
    description='Linux 下的划词翻译工具，支持有道智云等多种翻译服务',
    long_description='查看 `GitHub <https://github.com/bianjp/popup-dict>`_',

    platforms='Linux',
    python_requires='>= 3.5',
    install_requires=[
        'psutil',
        'requests',
    ],

    entry_points={
        'console_scripts': [
            'popup-dict = popupdict.main:main',
        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: GTK',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: End Users/Desktop',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Desktop Environment',
        'Topic :: Education',
    ],

)
