from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in leadcrm/__init__.py
from leadcrm import __version__ as version

setup(
	name="leadcrm",
	version=version,
	description="CRM",
	author="Soham",
	author_email="soham.pawar@erpdata.in",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
