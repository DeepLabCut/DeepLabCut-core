#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
deeplabcutcore Toolbox (deeplabcut.org)
© A. & M. Mathis Labs

Licensed under GNU Lesser General Public License v3.0
"""


import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="deeplabcutcore",
    version="0.0",
    author="A. & M.W. Mathis Labs",
    author_email="alexander@deeplabcut.org",
    description="Headless DeepLabCut",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/deeplabcutcore/deeplabcutcorecore",
    install_requires=[
        "certifi",
        "chardet",
        "click",
        "easydict",
        "h5py~=2.7",
        "intel-openmp",
        "imgaug",
        "ipython",
        "ipython-genutils",
        "matplotlib==3.0.3",
        "moviepy<=1.0.1",
        "numpy==1.16.4",
        "opencv-python-headless~=3.4",
        "pandas",
        "patsy",
        "python-dateutil",
        "pyyaml>=5.1",
        "requests",
        "ruamel.yaml~=0.15",
        "setuptools",
        "scikit-image",
        "scikit-learn",
        "scipy",
        "six",
        "statsmodels",
        "tables",
        "tensorpack>=0.9.7.1",
        "tqdm",
        "wheel",
    ],
    scripts=["deeplabcutcore/pose_estimation_tensorflow/models/pretrained/download.sh"],
    packages=setuptools.find_packages(),
    data_files=[
        (
            "deeplabcutcore",
            [
                "deeplabcutcore/pose_cfg.yaml",
                "deeplabcutcore/pose_estimation_tensorflow/models/pretrained/pretrained_model_urls.yaml",
            ],
        )
    ],
    include_package_data=True,
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ),
    entry_points="",
)
