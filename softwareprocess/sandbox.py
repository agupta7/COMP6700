import pkg_resources

resource_package = __name__

str = pkg_resources.resource_string(resource_package, 'starLocations.cfg')

print str