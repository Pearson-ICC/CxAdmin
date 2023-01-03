def split_csv(every: int, csv: str) -> list[str]:
    """Helper function to split a csv into chunks of a given size."""
    lines = csv.splitlines()
    # get header row
    header = lines[0]
    # return ["\n".join(lines[i : i + every]) for i in range(0, len(lines), every)]
    return [
        (header + "\n" + "\n".join(lines[i : i + every]))
        for i in range(1, len(lines), every)
    ]
