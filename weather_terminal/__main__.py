# This is the application's entry point.

import sys
from argparse import ArgumentParser
from weather_terminal.core import parser_loader
from weather_terminal.core.forecast_type import ForecastType 
from weather_terminal.core.unit import Unit
from weather_terminal.core.set_unit_action import SetUnitAction

def _validate_forecast_args(args):
    if args.forecast_option is None:
        err_msg = (
            'One of these arguments must be used: '
            '-td/--today, -5d/--fivedays, -10d/--tendays, -w/weekend'
        )
        print(f'{argparser.prog}: error: {err_msg}', file=sys.stderr)
        sys.exit()

parsers = parser_loader.load('./weather_terminal/parsers')
argparser = ArgumentParser(
    prog='weather_terminal',
    description='Weather information from https://weather.com on your terminal'
)
required = argparser.add_argument_group('required arguments')
required.add_argument(
    '-p', '--parser', choices=parsers.keys(), required=True, dest='parser',
    help=('Specify which parser is going to be used to scrape weather information.')
)

required.add_argument(
    '-a', '--areacode', required=True, dest='area_code',
    help=('The area code to get the weather broadcast from - obtainable at https://weather.com')
)

unit_values = [name.title() for name, value in Unit.__members__.items()]
argparser.add_argument(
    '-u', '--unit', choices=unit_values, required=False, dest='unit', action=SetUnitAction,
    help=('Specify the unit that will be used to display the temperatures.')
)

argparser.add_argument(
    '-v', '--version', action='version', version='%(prog)s 1.0'
)

argparser.add_argument(
    '-td', '--today', dest='forecast_option', action='store_const', const=ForecastType.TODAY,
    help=('Show the weather forecast for the current day')
)

argparser.add_argument(
    '-5d', '--fivedays', dest='forecast_option', action='store_const', const=ForecastType.FIVEDAYS,
    help=('Show the weather forecast for the next five days')
)

argparser.add_argument(
    '-10d', '--tendays', dest='forecast_option', action='store_const', const=ForecastType.TENDAYS,
    help=('Show the weather forecast for the next ten days')
)

args = argparser.parse_args()
_validate_forecast_args(args)
cls = parsers[args.parser]
parser = cls()
results = parser.run(args)
for result in results:
    print(result)