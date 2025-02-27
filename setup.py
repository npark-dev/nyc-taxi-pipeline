from setuptools import setup, find_packages

setup(
    name="nyc-taxi-pipeline",
    version="0.1.0",
    description="NYC 택시 데이터 ETL 파이프라인",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pandas",
        "numpy",
        "pyarrow",
        "google-cloud-storage",
        "google-cloud-bigquery",
        "requests",
        "sodapy",
        "python-dotenv",
        "pyyaml",
    ],
    python_requires=">=3.8",
)
