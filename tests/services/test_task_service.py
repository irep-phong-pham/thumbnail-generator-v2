import pytest

from src.daos.task_dao.rds_task_dao import TaskDAO
from src.services import TaskService

from tests.mock.daos import mock_task_dao
from tests.mock.mock_config import USER_ID


@pytest.fixture()
def config(monkeypatch):
    monkeypatch.setattr(TaskDAO, 'get',
                        mock_task_dao.mock_get_tasks_by_user_id_succeed)
    monkeypatch.setattr(TaskDAO, 'get_all', mock_task_dao.mock_get_all_succeed)
    return {
        'user_id': USER_ID
    }


def test_get_tasks_by_user_id_succeed(config):
    task_svc = TaskService()
    tasks = task_svc.get_task(config['user_id'])

    assert len(tasks) == 5


def test_get_all_tasks_succeed(config):
    task_svc = TaskService()
    tasks = task_svc.get_all_tasks()

    assert len(tasks) == 7
