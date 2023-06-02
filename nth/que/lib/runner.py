from name_that_hash import runner


def verify_hashes_from_file(path):
    with open(path, "rb") as f:
        f.readline()
        hashes = [
            "5f4dcc3b5aa765d61d8327deb882cf99",
            "a6105c0a611b41b08f1209506350279e",
        ]  # Your hashes must be a list of hashes
        output = runner.api_return_hashes_as_dict(hashes)
        print(output)
