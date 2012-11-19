#
# ----------- setup.py
#

from setuptools import setup, Extension

setup(
    name="",
    packages=["mypkg"],
    author="Matthias Ihrke",
    author_email="mittner@nld.ds.mpg.de",
    ext_modules=[Extension("_mypkg",
                           sources=['mypkg.i, mypkg.c'],
                           depends=['mypkg.h'],
                           include_dirs=[np.get_include()],
#                           define_macros=macros,
                           swig_opts=['-modern','-py3'])]
      )


#
# ------------- mypkg.i
# 
%define DOCSTRING
"
This is a docstring
"
%enddef

%module(docstring=DOCSTRING) mypkg
%{
#define SWIG_FILE_WITH_INIT
%}

%init %{
  import_array();
%}

%header %{
#include "numpy/arrayobject.h"
%}

%feature("autodoc","1");
/** put in raw pointer
*/
%typemap(in) (double* x){
  $1 = (double*)PyArray_DATA($input);
}
%typemap(in) (double* y){
  $1 = (double*)PyArray_DATA($input);
}
void example(double* x, double* y);
%clear (double* x), (double* y);

