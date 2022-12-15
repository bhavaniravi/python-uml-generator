# GitHub Custom Action - Python ERD Diagram Generator

The idea started from my [UML generator blog post](https://www.bhavaniravi.com/python/generate-uml-diagrams-from-python-code). There was no github action associated with it, so why not create one.

## How it works?

1. The workflow needs basic python setup step. You can customize it to your python version
2. The workflow installs `pylint` and `graphviz` and uses that to generate class diagrams. You can generate it in supported formats
3. The generated files get uploaded to the repo
4. If it's an image it gets referenced in the PR for review

The example workflow is under [.github/workflows/action.yml](.github/workflows/action.yml)





