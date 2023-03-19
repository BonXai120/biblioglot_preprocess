def to_dict(obj):
    if isinstance(obj, (list, tuple)):
        return [to_dict(item) for item in obj]
    elif isinstance(obj, dict):
        return {key: to_dict(value) for key, value in obj.items()}
    elif hasattr(obj, '__dict__'):
        return to_dict(obj.__dict__)
    else:
        return obj