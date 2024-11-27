import pytest
from task_2 import create_folder, get_info_folder, URL, HEADERS
import requests


@pytest.fixture
def cleanup_folder():
    folder_name = "test_folder"
    yield folder_name

    _ = requests.delete(f"{URL}?path={folder_name}", headers=HEADERS)


def test_create_folder(cleanup_folder) -> None:

    folder_name = cleanup_folder
    response = create_folder(folder_name)
    assert response.status_code == 201

    info_response = get_info_folder(folder_name)
    assert info_response.status_code == 200


def test_create_existing_folder(cleanup_folder) -> None:
    folder_name = cleanup_folder

    _ = create_folder(folder_name)

    response = create_folder(folder_name)
    assert response.status_code == 409
    assert "already exists" in response.text
