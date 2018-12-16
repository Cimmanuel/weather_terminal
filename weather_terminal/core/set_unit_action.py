from argparse import Action
import Unit

class SetUnitAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        unit = Unit[values.upper()]
        setattr(namespace, self.dest, unit)