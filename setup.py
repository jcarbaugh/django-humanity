from distutils.core import setup

setup(
    name="django-humanity",
    version="0.2",
    author="Jeremy Carbaugh",
    author_email="jcarbaugh@gmail.com",
    description="Form for math-based human verification",
    long_description=open("README.rst").read(),
    url="https://github.com/jcarbaugh/django-humanity",
    license='BSD',
    packages=["humanity"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
