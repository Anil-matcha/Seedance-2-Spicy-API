from setuptools import setup

setup(
    name="seedance-2-spicy-api",
    version="0.1.0",
    author="Anil Matcha",
    description="Python wrapper for ByteDance's Seedance 2 Spicy API — the relaxed-moderation VIP tier of Seedance 2.0/2 Mini, delivered via MuAPI. Text-to-Video, Image-to-Video, and Omni Reference with reduced content-safety filtering.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    py_modules=["seedance_2_spicy_api", "mcp_server"],
    install_requires=[
        "requests",
        "python-dotenv",
        "mcp[cli]"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
