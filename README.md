# Evaluation of multilayer community detection based on information compression
This is the repository which evaluates the community detection algorithms used in the article Community Detection in Multi-Partite Multi-Relational Networks Based on Information Compression. The evaluation metric used is NMI.
## Usage

### How to run the evaluation code
The networks for evaluation have been pre-generated. The ground truth as well as predicted communities are also pre-generated.
Simply run the following python file to generate plots for different values of alpha, d, p and mu: 

`python3 compute_nmi.py`

If you want to run this on python2.7, you might have to make some modifications to this file.

To run on custom networks, update the paths to ground truth communities and predicted communities in the compute_nmi.py file

## Usage of community detection code. 
Copied from the this github repository - [hetero_scala](https://github.com/weichuliu/hetero_scala)
This is a scala project. It is built with sbt.

Suppose you have java and sbt on your system.

To compile project into a single jar file:
$ cd /path/to/hetero_scala
hetero_scala $ sbt assembly
... (scala magics)
hetero_scala $ ls target/scala-2.10/hetcom.jar
To run the algorithm using jar file:
Get a help doc by calling without arguments
$ java -jar /path/to/hetcom.jar
usage:
  ...
  ...

$ java -jar /path/to/hetcom.jar ...(arguments)
 or
$ java -cp /path/to/hetcom.jar {package}.{object} ...(arguments)
To use it in REPL:
hetero_scala $ sbt console

For more detail, visit the [original repository](https://github.com/weichuliu/hetero_scala)
