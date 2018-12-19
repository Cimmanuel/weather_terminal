from argparse import Action
from .unit import Unit

class SetUnitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        unit = Unit[values.upper()]
        setattr(namespace, self.dest, unit)