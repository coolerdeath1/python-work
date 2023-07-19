import pkg_resources

def get_installed_modules():
    installed_modules = [d for d in pkg_resources.working_set]
    installed_modules.sort(key=lambda x: str(x).lower())
    for module in installed_modules:
        print(f"{module.key}=={module.version}")

# Example usage
get_installed_modules()