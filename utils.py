
def make_map_func(input_start, input_end, output_start, output_end):
    slope = (output_end - output_start) / (input_end - input_start)

    def result(value):
      return round(output_start + slope * (value - input_start))

    return result
