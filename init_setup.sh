echo [$(date)]: "START"
echo [$(date)]: "creating env with python 3.8 version"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activating enviornment "
source activate ./env
echo [$(date)]: "installing the development requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"