# Copyright 2017 Daniel Hilst Selli
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License. 
# 

'''
Function cheats that I keep below the sleeve.
'''

from functools import partial, reduce
import operator as o 

def compose(*funcs):
    'Return compositon of funcs'
    def compose2(f, g):
        return lambda *args, **kwargs: f(g(*args, **kwargs))
    return reduce(compose2, funcs)

def curry(f):
    'Return curried version of f'
    def _(arg):
        try:
            return f(arg)
        except TypeError:
            return curry(partial(f, arg))
    return _

def fswap(f):
    'Given f(a,b) returns f(b,a)'
    return lambda a,b: f(b,a)

def operator_fcty(op, other, swap=False):
    'Operator factory'
    op = fswap(op) if swap else op
    return partial(op, other)

class Lambda(object):
    'Lambda expressions'

    def __le__(self, other):
        return operator_fcty(o.le, other, True)

    def __lt__(self, other):
        return operator_fcty(o.lt, other, True)

    def __gt__(self, other):
        return operator_fcty(o.gt, other, True)

    def __ge__(self, other):
        return operator_fcty(o.ge, other, True)

    def __rle__(self, other):
        return operator_fcty(o.le, other)

    def __rlt__(self, other):
        return operator_fcty(o.lt, other)

    def __rgt__(self, other):
        return operator_fcty(o.gt, other)

    def __rge__(self, other):
        return operator_fcty(o.ge, other)

    def __eq__(self, other):
        return operator_fcty(o.eq, other)
    __req__ = __eq__

    def __mul__(self, other):
        return operator_fcty(o.mul, other)
    __rmul__ = __mul__

    def __add__(self, other):
        return operator_fcty(o.add, other)
    __radd__ = __add__

    def __sub__(self, other):
        return operator_fcty(o.sub, other, True)
    
    def __rsub__(self, other):
        return operator_fcty(o.sub, other)

    def __rfloordiv__(self, other):
        return operator_fcty(o.floordiv, other)

    def __floordiv__(self, other):
        return operator_fcty(o.floordiv, other, True)

    def __rtruediv__(self, other):
        return operator_fcty(o.truediv, other)

    def __truediv__(self, other):
        return operator_fcty(o.truediv, other, True)

LAMBDA = Lambda()
