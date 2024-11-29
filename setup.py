from setuptools import setup, find_packages

setup(
    name="agent_eval_harness",
    version="0.1.0",
    description="",
    python_requires=">=3.9",
    packages=find_packages(include=["agent_eval_harness*"]),
    install_requires=[
        'datasets',
        'weave',
        'huggingface-hub',
        'python-dotenv',
        'setuptools>=48.0.0',
        'inspect_ai @ git+https://github.com/UKGovernmentBEIS/inspect_ai@4c189e53f30a06b740df2b2ce5b3aa2dd79c57ee',
        'inspect-evals @ git+https://github.com/UKGovernmentBEIS/inspect_evals@5341ed9e6b1af43d8534b1d3c310115f092f16bc',
        'azure-mgmt-compute>=29.1.0',
        'azure-mgmt-network>=25.1.0',
        'azure-mgmt-resource>=23.0.1',
        'azure-identity>=1.12.0',
        'paramiko',
        'tenacity>=8.2.0'
    ],
    entry_points={
        'console_scripts': [
            'agent-eval=agent_eval_harness.cli:main',
            'agent-upload=agent_eval_harness.utils.upload:upload_results',
        ],
    },
)
