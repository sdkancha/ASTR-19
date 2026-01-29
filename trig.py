import math
def sin_table(x1, x2, entries):
    table = []
    step_size = (x2 - x1) / (entries - 1)

    for i in range(entries):
        x = x1 + i * step_size
        y = math.sin(x)
        table.append((x, y))
    return table

def table_print(table):

    print(f"{'x':<15} | {'sin(x)':<15}")
    print("-" * 33)
    for x, y in table:
        print(f"{x:<15.6f} | {y:<15.6f}")

def main():
    start = 0.0
    end = 2.0
    entries = 1000
    print(f"Generating table for sin(x) from x = {start} to x = {end} with {entries} entries.")
    calc_sin_tables = sin_table(start, end, entries)
    table_print(calc_sin_tables)

if __name__ == "__main__":
    main()