# Tensorflow for Apple Silicon

This simple documents will help you to install Tensorflow on Apple Silicon.

Create Environment to isolate packages

```
python3 -m venv ~/apple-metal
```

Activate Environment

```
source ~/apple-metal/bin/activate
```

Install Tensorflow

```
python -m pip install tensorflow
```

Then, install Metal Converter

```
python -m pip install tensorflow-metal
```

### Plugins

To use Tensorflow to build ML models, you need to install some plugins.

```
python -m pip install matplotlib
python -m pip install numpy
python -m pip install pandas
python -m pip install scikit-learn
python -m pip install statsmodels
```

# Demo

```
python examples/main.py
```
