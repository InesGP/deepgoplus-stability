# DeepGOPlus-stability

The perturbed results aren't provided, but the original data can be found at can be found at ```http://deepgoplus.bio2vec.net/data``` labelled as version 1.0.6.


## Instructions
* In order to run the full set of experiments, the DeepGOPlus repository and the significant_digits (v.0.0) repository will have to be cloned
	* ```compute_sig_protein.py``` is to be added to the significant_digits package
	* ```main.py``` and ```evaluate_deepgoplus.py``` are to replace the files of the same name in the DeepGOPlus package
* In order to create the Verificarlo Python, Verrou TF or Verrou All  containers, select the appropriate Dockerfile in the Dockerfiles folder
* User ```docker build -t imageName .``` to build the image for deepgoplus fuzzy model and convert if needed to Singularity
* Run a container of the image
* DeepGOPlus is already installed in the image, but to get further details on how to run the model consult [here](https://github.com/bio-ontology-research-group/deepgoplus)
* For Verificarlo Python, set ```echo "libinterflop_mca.so -m MODE --precision-binary32=FLOAT_PRECISION --precision-binary64=DOUBLE_PRECISION" > $VFC_BACKENDS_FROM_FILE``` to preferred mode or precision, however the results for Verificarlo Python were obtained with the default settings 
	* To obtain the protein predictions, run the below command
	```python3 /deepgoplus/deepgoplus/main.py -dr /workdir/data-1.0.6/data -if INPUT_FILE -of OUTPUT_FILE```
* For Verrou, simply run the below command and pass in the appropriate exclusion file to instrument either the entire program or just Tensorflow
```
valgrind --tool=verrou --rounding-mode=random --mca-mode=rr -s --check-nan=no --exclude=ABSOLUTE_EXCLUSION_FILEPATH --mca-precision-double=53 --mca-precision-float=24 python3 /deepgoplus/deepgoplus/main.py -dr /workdir/data-1.0.6/data -if INPUT_FILE -of OUTPUT_FILE
```
* In order to experiment with reduced precision using Verrou, use the below command
```
valgrind --tool=verrou --backend=vprec --rounding-mode=random -s --check-nan=no --exclude=ABSOLUTE_EXCLUSION_FILEPATH --vprec-precision-binary64=DOUBLE_PRECISION --vprec-range-binary64=DOUBLE_RANGE --vprec-precision-binary32=FLOAT_PRECISION --vprec-range-binary32=FLOAT_RANGE python3 /deepgoplus/deepgoplus/main.py -dr /workdir/data-1.0.6/data -if INPUT_FILE -of OUTPUT_FILE
```
* Metrics are calculated as shown below in an IEEE environment and so should not be run in any of the perturbed containers
```
python3 /deepgoplus/evaluate_deepgoplus.py -dr /workdir/data-1.0.6 -tsdf INPUT_PREDICTIONS -o ONTOLOGY_CLASS
```
* To calculate significant digits, run ```python3 compute_sig.py METRIC_OUTPUT_NAME REFERENCE_FILE_NAME SAMPLE_FILE``` to calculate the metrics and ```python3 compute_sig_protein.py PROTEIN_OUTPUT_NAME REFERENCE_FILE_NAME SAMPLE_FILE``` to calculate the significant digits of the protein predictions
* Copy the relevant files out of the container and set the paths to them in the Jupyter notebook
* From this point, run the code in the notebooks to generate statistics on the perturbed results and metrics in order to see if any perturbation can be found
* For additional information on instrumenting the code, consult [Fuzzy](https://github.com/verificarlo/fuzzy) and [Verrou](https://edf-hpc.github.io/verrou/vr-manual.html)
* For additional information on methodology, consult [this paper](https://arxiv.org/abs/2212.06361)

