from typing import List

from marker.v2.schema import Block
from marker.v2.schema.text.span import Span


class Line(Block):
    spans: List[Span]