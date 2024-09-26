conda create -n base-ai python=3.9
conda activate base-ai
conda install -c apple tensorflow-deps
python -m pip install tensorflow-macos==2.9
python -m pip install tensorflow-metal

echo "Running Hello world"
python main.py
