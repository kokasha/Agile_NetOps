
from operator import attrgetter
from pyangbind.lib.yangtypes import RestrictedPrecisionDecimalType
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import TypedListType
from pyangbind.lib.yangtypes import YANGBool
from pyangbind.lib.yangtypes import YANGListType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import ReferenceType
from pyangbind.lib.base import PybindBase
from decimal import Decimal
from bitarray import bitarray
import six

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
  import builtins as __builtin__
  long = int
  unicode = str
elif six.PY2:
  import __builtin__

class yc_Interface_interface__Interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module interface - based on the path /Interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__name','__mtu',)

  _yang_name = 'Interface'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='string', is_config=True)
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='uint16', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return [u'Interface']

  def _get_name(self):
    """
    Getter method for name, mapped from YANG variable /Interface/name (string)

    YANG Description: interface name
    """
    return self.__name
      
  def _set_name(self, v, load=False):
    """
    Setter method for name, mapped from YANG variable /Interface/name (string)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_name is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_name() directly.

    YANG Description: interface name
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='string', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """name must be of a type compatible with string""",
          'defined-type': "string",
          'generated-type': """YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='string', is_config=True)""",
        })

    self.__name = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_name(self):
    self.__name = YANGDynClass(base=unicode, is_leaf=True, yang_name="name", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='string', is_config=True)


  def _get_mtu(self):
    """
    Getter method for mtu, mapped from YANG variable /Interface/mtu (uint16)

    YANG Description:  Interface MTU
    """
    return self.__mtu
      
  def _set_mtu(self, v, load=False):
    """
    Setter method for mtu, mapped from YANG variable /Interface/mtu (uint16)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_mtu is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_mtu() directly.

    YANG Description:  Interface MTU
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='uint16', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """mtu must be of a type compatible with uint16""",
          'defined-type': "uint16",
          'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='uint16', is_config=True)""",
        })

    self.__mtu = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_mtu(self):
    self.__mtu = YANGDynClass(base=RestrictedClassType(base_type=int, restriction_dict={'range': ['0..65535']},int_size=16), is_leaf=True, yang_name="mtu", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='http://local.test/interface', defining_module='interface', yang_type='uint16', is_config=True)

  name = __builtin__.property(_get_name, _set_name)
  mtu = __builtin__.property(_get_mtu, _set_mtu)


  _pyangbind_elements = {'name': name, 'mtu': mtu, }


class interface(PybindBase):
  """
  This class was auto-generated by the PythonClass plugin for PYANG
  from YANG module interface - based on the path /interface. Each member element of
  the container is represented as a class variable - with a specific
  YANG type.
  """
  __slots__ = ('_pybind_generated_by', '_path_helper', '_yang_name', '_extmethods', '__Interface',)

  _yang_name = 'interface'

  _pybind_generated_by = 'container'

  def __init__(self, *args, **kwargs):

    self._path_helper = False

    self._extmethods = False
    self.__Interface = YANGDynClass(base=yc_Interface_interface__Interface, is_container='container', yang_name="Interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://local.test/interface', defining_module='interface', yang_type='container', is_config=True)

    load = kwargs.pop("load", None)
    if args:
      if len(args) > 1:
        raise TypeError("cannot create a YANG container with >1 argument")
      all_attr = True
      for e in self._pyangbind_elements:
        if not hasattr(args[0], e):
          all_attr = False
          break
      if not all_attr:
        raise ValueError("Supplied object did not have the correct attributes")
      for e in self._pyangbind_elements:
        nobj = getattr(args[0], e)
        if nobj._changed() is False:
          continue
        setmethod = getattr(self, "_set_%s" % e)
        if load is None:
          setmethod(getattr(args[0], e))
        else:
          setmethod(getattr(args[0], e), load=load)

  def _path(self):
    if hasattr(self, "_parent"):
      return self._parent._path()+[self._yang_name]
    else:
      return []

  def _get_Interface(self):
    """
    Getter method for Interface, mapped from YANG variable /Interface (container)
    """
    return self.__Interface
      
  def _set_Interface(self, v, load=False):
    """
    Setter method for Interface, mapped from YANG variable /Interface (container)
    If this variable is read-only (config: false) in the
    source YANG file, then _set_Interface is considered as a private
    method. Backends looking to populate this variable should
    do so via calling thisObj._set_Interface() directly.
    """
    if hasattr(v, "_utype"):
      v = v._utype(v)
    try:
      t = YANGDynClass(v,base=yc_Interface_interface__Interface, is_container='container', yang_name="Interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://local.test/interface', defining_module='interface', yang_type='container', is_config=True)
    except (TypeError, ValueError):
      raise ValueError({
          'error-string': """Interface must be of a type compatible with container""",
          'defined-type': "container",
          'generated-type': """YANGDynClass(base=yc_Interface_interface__Interface, is_container='container', yang_name="Interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://local.test/interface', defining_module='interface', yang_type='container', is_config=True)""",
        })

    self.__Interface = t
    if hasattr(self, '_set'):
      self._set()

  def _unset_Interface(self):
    self.__Interface = YANGDynClass(base=yc_Interface_interface__Interface, is_container='container', yang_name="Interface", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='http://local.test/interface', defining_module='interface', yang_type='container', is_config=True)

  Interface = __builtin__.property(_get_Interface, _set_Interface)


  _pyangbind_elements = {'Interface': Interface, }


