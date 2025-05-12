# test_task_manager.py
import pytest
from task_manager import TaskManager

def test_add_and_list_tasks(regtest):
    """
    1. Creează o instanță a clasei TaskManager.
    2. Adaugă două taskuri
    3. Obține lista taskurilor cu metoda list_tasks().
    4. Scrie rezultatul în regtest (folosind regtest.write()).
    """
    tm = TaskManager()
    tm.add_task("Primul task")
    tm.add_task("Al doilea task")
    regtest.write(tm.list_tasks() + "\n")

def test_mark_done_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Marchează acest task ca finalizat (index 0).
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda mark_done(index).
    """
    tm = TaskManager()
    tm.add_task("Un task de facut")
    tm.mark_done(0)
    regtest.write(tm.list_tasks() + "\n")

def test_delete_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă două taskuri
    3. Șterge primul task (index 0).
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda delete_task(index).
    """
    tm = TaskManager()
    tm.add_task("Task 1")
    tm.add_task("Task 2")
    tm.delete_task(0)
    regtest.write(tm.list_tasks() + "\n")

def test_edit_task(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Editează descrierea acestui task cu o descriere nouă
    4. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: folosește metoda edit_task(index, noua_descriere).
    """
    tm = TaskManager()
    tm.add_task("Task initial")
    tm.edit_task(0, "Task editat")
    regtest.write(tm.list_tasks() + "\n")

def test_combination_operations(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă două taskuri
    3. Marchează al doilea task ca finalizat.
    4. Editează primul task cu o descriere nouă
    5. Șterge al doilea task.
    6. Obține lista taskurilor și scrie rezultatul în regtest.
    
    Hint: combină metodele add_task, mark_done, edit_task, delete_task.
    """
    tm = TaskManager()
    tm.add_task("Task unu")
    tm.add_task("Task doi")
    tm.mark_done(1)
    tm.edit_task(0, "Task 1 editat")
    tm.delete_task(1)
    regtest.write(tm.list_tasks() + "\n")

def test_invalid_index_mark_done(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să marchezi ca finalizat un index invalid
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: folosește try-except și str(e) ca să obții mesajul excepției.
    """
    tm = TaskManager()
    tm.add_task("Task existent")
    try:
        tm.mark_done(5)
    except IndexError as e:
        regtest.write(str(e) + "\n")

def test_invalid_index_delete(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să ștergi un task cu index invalid (ex: index -1).
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: la fel ca la test_invalid_index_mark_done.
    """
    tm = TaskManager()
    tm.add_task("Task de sters")
    try:
        tm.delete_task(-1)
    except IndexError as e:
        regtest.write(str(e) + "\n")

def test_invalid_index_edit(regtest):
    """
    1. Creează o instanță TaskManager.
    2. Adaugă un task
    3. Încearcă să editezi un index invalid (ex: index 2) cu o descriere nouă.
    4. Prinde excepția IndexError și scrie mesajul ei în regtest.
    
    Hint: folosește try-except și scrie mesajul excepției.
    """
    tm = TaskManager()
    tm.add_task("Task editabil")
    try:
        tm.edit_task(2, "Noua descriere")
    except IndexError as e:
        regtest.write(str(e) + "\n")
