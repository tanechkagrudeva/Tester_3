def get_val(collection, key, default='git'):
    if key in collection:
        return collection[key]
    elif key not in collection:
        return default

data = {"vcs": "mercurial"}

print(get_val(data, "vcs"))

print(get_val(data, "vcs", "git"))

data = {}

print(get_val({}, "vcs", "git"))

print(get_val({}, "vcs", "bazaar"))