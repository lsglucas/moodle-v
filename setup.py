import setuptools

setuptools.setup(
    name="moodleapi",
    version="1.3.2",
    author="Daniel Kauffmann",
    author_email="danielvenna2@gmail.com",
    description="MoodleAPI Package for Bot usable",
    long_description='Nothing here',
    long_description_content_type="text/markdown",
    url="https://github.com/lsglucas/DiscordMackBot",
    packages=setuptools.find_packages(exclude=['*bot*', '*secret.py*']),#['moodleapi', 'moodleapi/data'],
    install_requires=['requests', 'cryptography', 'pandas'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)