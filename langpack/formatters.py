def format_datetime(value, format='default', translator=None):
    if _is_key(format):
        format = translator.get_template('datetime.formats.' + format, default=format)

    if '%a' in format:
        short_day_names = translator.get_template('datetime.short_day_names', default=[])
        format = format.replace('%a', short_day_names[value.isoweekday()])

    if '%A' in format:
        day_names = translator.get_template('datetime.day_names', default=[])
        format = format.replace('%A', day_names[value.isoweekday()])

    if '%b' in format:
        short_month_names = translator.get_template('datetime.short_month_names', default=[])
        format = format.replace('%b', short_month_names[value.month])

    if '%B' in format:
        month_names = translator.get_template('datetime.month_names', default=[])
        format = format.replace('%B', month_names[value.month])

    return value.strftime(format)


def _is_key(value):
    return value.lower() and ' ' not in value
