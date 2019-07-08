# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.0
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (3, 0, 0):
    raise RuntimeError('Python 3.0 or later required')

# Import the low-level C/C++ module
if __package__ or '.' in __name__:
    from . import _cpgnumpy
else:
    import _cpgnumpy

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if name == "thisown":
        return self.this.own(value)
    if name == "this":
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if not static:
        object.__setattr__(self, name, value)
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if name == "thisown":
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class cPgNumpy(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr

    def __init__(self, *args):
        _cpgnumpy.cPgNumpy_swiginit(self, _cpgnumpy.new_cPgNumpy(*args))
    __swig_destroy__ = _cpgnumpy.delete_cPgNumpy

    def open(self, *args):
        return _cpgnumpy.cPgNumpy_open(self, *args)

    def execute(self, *args):
        return _cpgnumpy.cPgNumpy_execute(self, *args)

    def fetchall(self):
        return _cpgnumpy.cPgNumpy_fetchall(self)

    def write(self, filename=None):
        return _cpgnumpy.cPgNumpy_write(self, filename)

    def use_text(self):
        return _cpgnumpy.cPgNumpy_use_text(self)

    def set_decorators(self, decorate):
        return _cpgnumpy.cPgNumpy_set_decorators(self, decorate)

    def execwrite(self, query, filename=None):
        return _cpgnumpy.cPgNumpy_execwrite(self, query, filename)

    def set_fetch_count(self, fetchcount):
        return _cpgnumpy.cPgNumpy_set_fetch_count(self, fetchcount)

    def ntuples(self):
        return _cpgnumpy.cPgNumpy_ntuples(self)

    def nfields(self):
        return _cpgnumpy.cPgNumpy_nfields(self)

    def status(self):
        return _cpgnumpy.cPgNumpy_status(self)

    def set_field_lengths(self, flenDict):
        return _cpgnumpy.cPgNumpy_set_field_lengths(self, flenDict)

    def clear_field_lengths(self):
        return _cpgnumpy.cPgNumpy_clear_field_lengths(self)

    def clear(self):
        return _cpgnumpy.cPgNumpy_clear(self)

    def close(self):
        return _cpgnumpy.cPgNumpy_close(self)

# Register cPgNumpy in _cpgnumpy:
_cpgnumpy.cPgNumpy_swigregister(cPgNumpy)
