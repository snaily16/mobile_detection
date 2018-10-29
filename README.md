## Shoes Detection

## Dependencies

Python3, tensorflow 1.0, numpy, opencv 3.

### Getting started

You can choose _one_ of the following three ways to get started with darkflow.

1. Just build the Cython extensions in place. NOTE: If installing this way you will have to use `./flow` in the cloned darkflow directory instead of `flow` as darkflow is not installed globally.
    ```
    python3 setup.py build_ext --inplace
    ```

2. Let pip install darkflow globally in dev mode (still globally accessible, but changes to the code immediately take effect)
    ```
    pip install -e .
    ```

3. Install with pip globally
    ```
    pip install .
    ```

4. After building the Cython extension using any of above three methods, run this command.
	'''
	python3 realtime.py
	'''
