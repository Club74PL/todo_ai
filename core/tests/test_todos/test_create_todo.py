import uuid
import pytest
from freezegun import freeze_time

from core.todos.create_todo import init_todo

from core.todos.todo import Todo, Status

from unittest.mock import patch
from datetime import timedelta, datetime


def test_create_basic_valid_todo() -> None:
    mock_uuid4 = uuid.UUID('352c9582-2d41-4ba7-9b9e-d8e7d72ee7ac')

    with freeze_time('2024-12-12'), patch('uuid.uuid4', return_value=mock_uuid4):
        todo: Todo = init_todo(
            name='Learn Flask'
        )

    assert todo == Todo(
        name='Learn Flask',

    )


def test_create_todo_with_empty_name():
    with pytest.raises(ValueError, match='Task name is required.'):
        init_todo(name='')


def test_create_todo_invalid_name():
    with pytest.raises(ValueError, match='Task name is required.'):
        init_todo(name=' ')


@pytest.mark.skip(reason='Not implemented yet.')
def test_create_todo_with_all_options():
    with freeze_time('2024-12-12'):
        start_datetime = datetime.now() + timedelta(days=1)
        data = {
            'name': 'Learn flask',
            'description': 'Learn Flask in 2025',
            'start_dt': start_datetime,
            'duration': timedelta(minutes=10),
            'type': 'workshop',
            'priority': 'critical',
        }

        todo = init_todo(**data)

        assert todo == {
            **data,
            'id': 1,
            'status': 'pending',
            'created_at': datetime(2024, 12, 12, )
        }


def test_create_todo_with_past_start_date():
    pass


def test_create_todo_with_non_positive_duration():
    pass


def test_create_todo_with_non_positive_estimated_duration():
    pass
