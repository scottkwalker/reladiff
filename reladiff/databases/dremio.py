from sqeleton.databases import dremio as d
from .base import ReladiffDialect


class Dialect(d.Dialect, d.Mixin_MD5, d.Mixin_NormalizeValue, ReladiffDialect):
    pass


class Dremio(d.Dremio):
    dialect = Dialect()
