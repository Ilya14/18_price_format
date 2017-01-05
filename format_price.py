def format_price(price):
    float_price = float(price)
    sign = '-' if float_price < 0 else ''
    digits_count = 2
    float_price = round(abs(float_price), digits_count)
    whole_part = int(float_price)
    remove_signs_count = 2
    fractional_part = str(round(float_price - whole_part, digits_count))[remove_signs_count:]
    whole_part = str(whole_part)

    positions_count = 3
    formatted_price = ''
    while whole_part:
        whole_part, last3 = whole_part[:-positions_count], whole_part[-positions_count:]
        formatted_price = '{0} {1}'.format(last3, formatted_price) if formatted_price else last3

    formatted_price = '{0}{1}{2}'.format(
        sign,
        formatted_price,
        ',{0}'.format(fractional_part) if fractional_part != '0' else ''
    )

    return formatted_price

if __name__ == '__main__':
    import argparse
    import logging

    def get_input_data():
        parser = argparse.ArgumentParser(description='Script for price formatting')
        parser.add_argument('price', help='Price string')
        return parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format=u'[%(filename)s#] %(levelname)-8s [%(asctime)s] %(message)s',
        datefmt=u'%m/%d/%Y %I:%M:%S %p'
    )

    args = get_input_data()
    price_string = args.price

    try:
        formatted_price = format_price(price_string)
        logging.info('Formatted price: %s', formatted_price)
    except ValueError as error:
        logging.exception('Incorrect price string')
