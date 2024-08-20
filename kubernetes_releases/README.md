Utility to get the last few Kubernetes releases for:
1. Upstream Kubernetes
2. Amazon EKS
3. Azure AKS
4. Google GKE

It also displays below info:
1. Release data
2. End of Life date
3. Latest release
4. Latest release date

# SAMPLE OUTPUT
```
Product       Version  Release Date    End of Life Date    Latest Release    Latest Release Date
----------  ---------  --------------  ------------------  ----------------  ---------------------
kubernetes       1.31  2024-08-13      2025-10-28          1.31.0            2024-08-13

Product       Version  Release Date    End of Life Date    Latest Release    Latest Release Date
----------  ---------  --------------  ------------------  ----------------  ---------------------
kubernetes       1.30  2024-04-17      2025-06-28          1.30.4            2024-08-14
eks              1.30  2024-05-23      2025-07-23          1.30-eks-6        2024-08-09

Product       Version  Release Date    End of Life Date    Latest Release      Latest Release Date
----------  ---------  --------------  ------------------  ------------------  ---------------------
kubernetes       1.29  2023-12-13      2025-02-28          1.29.8              2024-08-14
eks              1.29  2024-01-23      2025-03-23          1.29-eks-11         2024-08-09
aks              1.29  2024-03-18      2025-01-31          N/A                 N/A
gke              1.29  2024-01-26      2025-03-21          1.29.7-gke.1274000  2024-08-14

Product       Version  Release Date    End of Life Date    Latest Release       Latest Release Date
----------  ---------  --------------  ------------------  -------------------  ---------------------
kubernetes       1.28  2023-08-15      2024-10-28          1.28.13              2024-08-14
eks              1.28  2023-09-26      2024-11-26          1.28-eks-17          2024-08-09
aks              1.28  2023-11-07      2024-11-30          N/A                  N/A
gke              1.28  2023-12-04      2025-02-04          1.28.12-gke.1179000  2024-08-14

Product       Version  Release Date    End of Life Date    Latest Release       Latest Release Date
----------  ---------  --------------  ------------------  -------------------  ---------------------
kubernetes       1.27  2023-04-11      2024-06-28          1.27.16              2024-07-17
eks              1.27  2023-05-24      2024-07-24          1.27-eks-21          2024-08-09
aks              1.27  2023-08-16      2024-07-31          N/A                  N/A
gke              1.27  2023-06-15      2024-08-31          1.27.16-gke.1148000  2024-08-14

Product      Version  Release Date    End of Life Date    Latest Release       Latest Release Date
---------  ---------  --------------  ------------------  -------------------  ---------------------
eks             1.26  2023-04-11      2024-06-11          1.26-eks-22          2024-08-09
aks             1.26  2023-04-18      2024-04-11          N/A                  N/A
gke             1.26  2023-03-31      2024-06-30          1.26.15-gke.1469001  2024-07-03

Product      Version  Release Date    End of Life Date    Latest Release       Latest Release Date
---------  ---------  --------------  ------------------  -------------------  ---------------------
aks             1.25  2022-12-14      2024-01-14          N/A                  N/A
gke             1.25  2022-12-14      2024-03-30          1.25.16-gke.1759000  2024-04-18
```%
