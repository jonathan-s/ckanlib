# ckanlib

A pof wrapper for ckan


# Usage of library

    import ckanlib

    wrapper = ckanlib.CKAN()

    # getting the count of datasets
    print wrapper.total_datasets() # 16

    # calculate internal and external resources
    print wrapper.external_vs_internal()
    # {'external': 8, 'internal': 10}

    # getting packages in python data structure
    packages = wrapper.packages() # a list
    package = packages[0]

    # access a package through dot notation
    package.resources # a list of resources

    # it's possible to continue using dot notation
    package.resources[0].name

## License
MIT license
