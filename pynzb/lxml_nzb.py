from pynzb.base import BaseETreeNZBParser
from io import BytesIO

try:
    from lxml import etree
except ImportError:
    raise ImportError("You must have lxml installed before you can use the " +
                      "lxml NZB parser.")


class LXMLNZBParser(BaseETreeNZBParser):
    def get_etree_iter(self, xml, et=etree):
        return iter(et.iterparse(BytesIO(bytes(xml)), events=("start", "end")))
