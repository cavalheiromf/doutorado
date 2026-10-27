# Mock ETE4 module to prevent JCVI import crashes when plotting karyotypes and micro-synteny
class Tree:
    def __init__(self, *args, **kwargs):
        pass
