from marker.v2.schema import BlockTypes
from marker.v2.schema.blocks import Block


class Footnote(Block):
    block_type: BlockTypes = BlockTypes.Footnote
