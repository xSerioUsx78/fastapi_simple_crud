from fastapi import HTTPException, status


def get_object_or_404(obj):
    if obj is None:
        return HTTPException(status.HTTP_404_NOT_FOUND, "Object not found.")