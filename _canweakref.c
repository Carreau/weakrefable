#include <Python.h>
static PyObject *
canbeweakreferenced(PyObject *self, PyObject *args)
{
    const PyObject *obj;
    if (!PyArg_ParseTuple(args, "O", &obj))
        return NULL;
    if (PyType_SUPPORTS_WEAKREFS(Py_TYPE(obj))) {
        Py_INCREF(Py_True);
        Py_DECREF(obj);
        return Py_True;
    }
    Py_DECREF(obj);
    Py_INCREF(Py_False);
    return Py_False;
}


static PyMethodDef SpamMethods[] = {
    {"canbeweakreferenced",  canbeweakreferenced, METH_VARARGS, "Execute a shell command."},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef spammodule = {
   PyModuleDef_HEAD_INIT,
   "_weakrefable",   /* name of module */
   NULL, /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   SpamMethods
};


PyMODINIT_FUNC
PyInit__weakrefable(void)
{
    return PyModule_Create(&spammodule);
}
