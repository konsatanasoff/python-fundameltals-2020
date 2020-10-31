def bar_filler(bar_list, check_bars):

    for index in range(check_bars):
        bar_list[index] = "%"

    return bar_list


bar = []
for n in range(10):
    bar.append(".")


percent = int(input())
bars_to_fill = percent // 10


filled = bar_filler(bar, bars_to_fill)

if percent < 100:
    print(f"{percent}% [{''.join(filled)}]")
    print(f"Still loading...")
else:
    print("100% Complete!")
    print("[%%%%%%%%%%]")