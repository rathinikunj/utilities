import requests
import tabulate

release_data = []
products = [
    "kubernetes",
    "amazon-eks",
    "azure-kubernetes-service",
    "google-kubernetes-engine",
]
table_header = [
    "Product",
    "Version",
    "Release Date",
    "End of Life Date",
    "Latest Release",
    "Latest Release Date",
]


def get_data(product, num_releases=5):
    global release_data
    url = f"https://endoflife.date/api/{product}.json"
    response = requests.get(url)
    data = response.json()
    count_releases = 0
    for d in data:
        count_releases += 1
        if count_releases > num_releases:
            break
        release_data.append(
            [
                product,
                d["cycle"],
                d["releaseDate"],
                d["eol"],
                d.get("latest", "N/A"),
                d.get("latestReleaseDate", "N/A"),
            ]
        )


def get_per_release_data(release_data):
    per_release_data = {}
    for (
        product,
        version,
        release_date,
        eol_date,
        latest_release,
        latest_release_date,
    ) in release_data:
        if product == "amazon-eks":
            product_alias = "eks"
        elif product == "azure-kubernetes-service":
            product_alias = "aks"
        elif product == "google-kubernetes-engine":
            product_alias = "gke"
        else:
            product_alias = product
        if version not in per_release_data:
            per_release_data[version] = []
        per_release_data[version].append(
            [
                product_alias,
                version,
                release_date,
                eol_date,
                latest_release,
                latest_release_date,
            ]
        )
    return per_release_data


for product in products:
    get_data(product)

per_release_data = get_per_release_data(release_data)
for version, data in per_release_data.items():
    print(tabulate.tabulate(data, headers=table_header, floatfmt=".2f") + "\n")
