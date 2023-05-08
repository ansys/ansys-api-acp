"""Installation file for the ansys-api-acp package"""

import os
from datetime import datetime

import setuptools

from ansys.tools.protoc_helper import CMDCLASS_OVERRIDE

# Get the long description from the README file
HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(HERE, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(os.path.join(HERE, "src", "ansys", "api", "acp", "VERSION"), encoding="utf-8") as f:
    version = f.read().strip()

package_name = "ansys-api-acp"

description = f"Autogenerated Python package for the Ansys Composite PrepPost (ACP) gRPC API."

if __name__ == "__main__":
    setuptools.setup(
        name=package_name,
        version=version,
        author="ANSYS, Inc.",
        author_email='support@ansys.com',
        description=description,
        long_description=long_description,
        long_description_content_type='text/markdown',
        url=f"https://github.com/ansys-internal/{package_name}",
        license="MIT",
        python_requires=">=3.7",
        install_requires=["grpcio~=1.17", "protobuf~=3.19"],
        package_dir = {"": "src"},
        packages=setuptools.find_namespace_packages("src", include=("ansys.*",)),
        package_data={
            "": ["*.proto", "*.pyi", "py.typed", "VERSION"],
        },
        entry_points={
            "ansys.tools.protoc_helper.proto_provider": [
                "ansys.api.acp.v0=ansys.api.acp.v0"
            ],
        },
        cmdclass=CMDCLASS_OVERRIDE
    )
