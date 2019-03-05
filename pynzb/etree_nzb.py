from pynzb.base import BaseETreeNZBParser

try:
    from xml.etree import ElementTree as Etree
except ImportError:
    raise ImportError("You must have either Python 2.5 or cElementTree " +
                      "installed before you can use the etree NZB parser.")

from io import StringIO


class ETreeNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, xml, et=Etree):
        return iter(et.iterparse(StringIO(xml), events=("start", "end")))
