from fastapi.testclient import TestClient
from app.main import app, INVALID_NUMBER_ERROR
from tests.test_data import \
    birth_numbers, expected_validity, expected_age, expected_gender, \
    expected_existence, expected_counts, expected_detailed_counts

TEST_DATASET_FILEPATH = "tests/test_fnr.txt"

client = TestClient(app)

def test_validate():
    for bn, valid in zip(birth_numbers, expected_validity):
        endpoint = f"/validate/{bn}"
        response = client.get(endpoint)
        assert response.status_code == 200
        assert response.json() == {"valid": valid}

def test_gender():
    for bn, gender in zip(birth_numbers, expected_gender):
        endpoint = f"/gender/{bn}"
        response = client.get(endpoint)
        assert response.status_code == 200
        if gender == -1:
            assert response.json() == INVALID_NUMBER_ERROR
        else:
            assert response.json() == {"gender": gender}

def test_age():
    for bn, age in zip(birth_numbers, expected_age):
        endpoint = f"/age/{bn}"
        response = client.get(endpoint)
        assert response.status_code == 200
        if age == -1:
            assert response.json() == INVALID_NUMBER_ERROR
        else:
            assert response.json() == {"age": age}

def test_existence():
    for bn, exists in zip(birth_numbers, expected_existence):
        endpoint = f"/dataset/exists/{bn}"
        response = client.get(endpoint)
        assert response.status_code == 200
        if exists == -1:
            assert response.json() == INVALID_NUMBER_ERROR
        else:
            assert response.json() == {"exists": exists}, f"{endpoint}, {exists}"

def write_test_dataset():
    with open(TEST_DATASET_FILEPATH, 'w') as file:
        for bn in birth_numbers:
            file.write(str(bn) + '\n')

def test_counts():
    write_test_dataset()
    endpoint = f"/dataset/counts/?dataset_filepath={TEST_DATASET_FILEPATH}"
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.json() == expected_counts

def test_detailed_counts():
    write_test_dataset()
    endpoint = f"/dataset/detailed_counts/?dataset_filepath={TEST_DATASET_FILEPATH}"
    response = client.get(endpoint)
    assert response.status_code == 200
    assert response.json() == expected_detailed_counts