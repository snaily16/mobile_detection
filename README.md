## Mobile Detection

## Dependencies

Python3, tensorflow 1.0, numpy, opencv 3.

### Getting started

You can choose _one_ of the following three ways to get started with darkflow.

1. Just build the Cython extensions in place. 
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

After building the Cython extension, run this command.
	```
    python3 realtime.py
    ```
    
It will start your videocamera and detect the mobile phones.


NOTE: If you want to change it to any other object detection then, 
* Open realtime.py
* Edit line no *39* : if label == 'cell phone' to any object name from cfg/coco.names.
