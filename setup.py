"""setup.py file."""
import uuid

from setuptools import setup, find_packages
try:
    # pip>=21.x.x
    from pip._internal.req.constructors import (
        install_req_from_parsed_requirement,
    )
except ImportError:
    # pip<=20.x.x
    def install_req_from_parsed_requirement(x):
        return x

try:
    # pip >=20
    from pip._internal.network.session import PipSession
    from pip._internal.req import parse_requirements
except ImportError:
    try:
        # 10.0.0 <= pip <= 19.3.1
        from pip._internal.download import PipSession
        from pip._internal.req import parse_requirements
    except ImportError:
        # pip <= 9.0.3
        from pip.download import PipSession
        from pip.req import parse_requirements

__author__ = 'Andreas Thienemann <andreas@bawue.net>'

install_reqs = parse_requirements('requirements.txt', session=uuid.uuid1())
install_reqs = [install_req_from_parsed_requirement(req) for req in install_reqs]

reqs = [str(ir.req) for ir in install_reqs]

setup(
    name="napalm-procurve",
    version="0.7.0",
    packages=find_packages(),
    author="Andreas Thienemann",
    author_email="andreas@bawue.net",
    description="Network Automation and Programmability Abstraction Layer (NAPALM) ProCurve driver",
    long_description="ProCurve driver support for Napalm network automation.",
    classifiers=[
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
    ],
    url="https://github.com/ixs/napalm-procurve",
    include_package_data=True,
    zip_safe=False,
    install_requires=reqs,
)
