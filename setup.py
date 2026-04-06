import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version = "0.0.1"

REPO_NAME = "TextSummarizer"
AUTHOR_USER_NAME = "Jayanth"
AUTHOR_EMAIL = "jayanththalla33@gmail.com"
SRC_REPO = "textsummarizer"


setuptools.setup(
    name=SRC_REPO,
    version=__version,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A text summarization package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),

)
