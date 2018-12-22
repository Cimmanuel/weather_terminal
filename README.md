# weather_terminal
This application gets weather forecast information from https://weather.com and presents it in a terminal.
However, you can create parsers for different weather websites. Put any parser you create in the weather_terminal/parsers directory. 

To get help starting the application, do:

`>>> python -m weather_terminal --help`

## Example
`>>> python -m weather_terminal --unit Celsius --areacode NIXX0008:1:NI --parser WeatherComParser --today`

NB: -a/--area_code and -p/--parser are required arguments while -u/--unit is optional and defaults to Fahrenheit if not supplied.
