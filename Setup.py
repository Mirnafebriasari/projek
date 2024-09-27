from setuptools import setup, find_packages

setup(
    name='motipy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',  # Pastikan Pillow terinstal
    ],
    description='A package for adjusting brightness of images.',
    author='Nama Anda',  # Ganti dengan nama Anda
    author_email='email@mirnhafebriasari.com',  # Ganti dengan email Anda
    url='https://github.com/username/motipy',  # Ganti dengan URL repositori yang sesuai
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Sesuaikan dengan versi Python yang dibutuhkan
)
