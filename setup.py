from setuptools import setup

setup(
    name="glid-3-xl",
    packages=["guided_diffusion", "encoders", "clip_custom"],
    install_requires=["blobfile>=1.0.5", "torch", "tqdm"],
    package_data={"": ["*.gz"]},
)
